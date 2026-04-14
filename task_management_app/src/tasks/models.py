from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from src.utils.db import Base


class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("user_Table.id", ondelete="CASCADE"))

## send the user_id in payload
