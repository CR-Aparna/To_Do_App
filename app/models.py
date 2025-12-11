from sqlalchemy import Column,Integer,String, Boolean,DateTime,Text
from sqlalchemy import func
from .database import Base 

class Task(Base):
    __tablename__="Tasks"
    task_id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    title=Column(String(250),nullable=False)
    description=Column(Text,nullable=True)
    status=Column(Boolean,default=False)
    created_at=Column(DateTime,server_default=func.now())
    