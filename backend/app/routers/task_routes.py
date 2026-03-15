"""
Task Routes
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid
from app.database import get_db
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import TaskService
from app.dependencies.auth_dependency import get_current_user
from app.models.user import User
from app.utils.response import success_response
from app.utils.logger import setup_logger

logger = setup_logger(__name__)
router = APIRouter()

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new task
    
    - **title**: Task title (required)
    - **description**: Task description (optional)
    - **status**: pending or completed (default: pending)
    """
    task_service = TaskService(db)
    task = task_service.create_task(task_data, current_user.id)
    logger.info(f"Task created: {task.id} by user {current_user.email}")
    return success_response(
        data={"task": TaskResponse.model_validate(task)},
        message="Task created successfully"
    )

@router.get("/", response_model=dict)
async def get_tasks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get all tasks
    
    - Users see only their tasks
    - Admins see all tasks
    """
    task_service = TaskService(db)
    tasks = task_service.get_tasks(current_user)
    return success_response(
        data={"tasks": [TaskResponse.model_validate(task) for task in tasks]},
        message="Tasks retrieved successfully"
    )

@router.get("/{task_id}", response_model=dict)
async def get_task(
    task_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get a specific task by ID
    
    - Users can only view their own tasks
    - Admins can view any task
    """
    task_service = TaskService(db)
    task = task_service.get_task_by_id(task_id, current_user)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return success_response(
        data={"task": TaskResponse.model_validate(task)},
        message="Task retrieved successfully"
    )

@router.put("/{task_id}", response_model=dict)
async def update_task(
    task_id: uuid.UUID,
    task_data: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update a task
    
    - Users can only update their own tasks
    - Admins can update any task
    """
    task_service = TaskService(db)
    task = task_service.update_task(task_id, task_data, current_user)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    logger.info(f"Task updated: {task_id} by user {current_user.email}")
    return success_response(
        data={"task": TaskResponse.model_validate(task)},
        message="Task updated successfully"
    )

@router.delete("/{task_id}", response_model=dict)
async def delete_task(
    task_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Delete a task
    
    - Users can only delete their own tasks
    - Admins can delete any task
    """
    task_service = TaskService(db)
    success = task_service.delete_task(task_id, current_user)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    logger.info(f"Task deleted: {task_id} by user {current_user.email}")
    return success_response(message="Task deleted successfully")
