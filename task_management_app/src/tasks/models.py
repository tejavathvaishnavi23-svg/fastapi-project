from sqlalchemy import Column, Integer, String, Boolean
from task_management_app.src.utils.db import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)
