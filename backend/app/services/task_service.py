"""
Task Service
"""
from sqlalchemy.orm import Session
from typing import List, Optional
import uuid
from app.models.task import Task
from app.models.user import User
from app.schemas.task_schema import TaskCreate, TaskUpdate

class TaskService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_task(self, task_data: TaskCreate, user_id: uuid.UUID) -> Task:
        """Create a new task"""
        new_task = Task(
            title=task_data.title,
            description=task_data.description,
            status=task_data.status,
            owner_id=user_id
        )
        
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)
        return new_task
    
    def get_tasks(self, current_user: User) -> List[Task]:
        """Get tasks based on user role"""
        if current_user.role == "admin":
            # Admin can see all tasks
            return self.db.query(Task).all()
        else:
            # Regular user can only see their tasks
            return self.db.query(Task).filter(Task.owner_id == current_user.id).all()
    
    def get_task_by_id(self, task_id: uuid.UUID, current_user: User) -> Optional[Task]:
        """Get a specific task by ID"""
        task = self.db.query(Task).filter(Task.id == task_id).first()
        
        if not task:
            return None
        
        # Check permissions
        if current_user.role != "admin" and task.owner_id != current_user.id:
            return None
        
        return task
    
    def update_task(self, task_id: uuid.UUID, task_data: TaskUpdate, current_user: User) -> Optional[Task]:
        """Update a task"""
        task = self.get_task_by_id(task_id, current_user)
        
        if not task:
            return None
        
        # Update fields
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.description is not None:
            task.description = task_data.description
        if task_data.status is not None:
            task.status = task_data.status
        
        self.db.commit()
        self.db.refresh(task)
        return task
    
    def delete_task(self, task_id: uuid.UUID, current_user: User) -> bool:
        """Delete a task"""
        task = self.db.query(Task).filter(Task.id == task_id).first()
        
        if not task:
            return False
        
        # Check permissions
        if current_user.role != "admin" and task.owner_id != current_user.id:
            return False
        
        self.db.delete(task)
        self.db.commit()
        return True
