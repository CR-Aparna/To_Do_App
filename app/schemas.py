from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str]

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str]=None
    description: Optional[str]=None
    status: Optional[bool]=None

class Task(TaskBase):
    task_id: int
    status: bool
    description: Optional[str]
    created_at:datetime

    model_config = {
        "from_attributes": True
    }
    