"""
Task Pydantic Schemas
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

class TaskCreate(BaseModel):
    """Schema for task creation"""
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    status: str = Field(default="pending", pattern="^(pending|completed)$")

class TaskUpdate(BaseModel):
    """Schema for task update"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    status: Optional[str] = Field(None, pattern="^(pending|completed)$")

class TaskResponse(BaseModel):
    """Schema for task response"""
    id: uuid.UUID
    title: str
    description: Optional[str]
    status: str
    owner_id: uuid.UUID
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True
