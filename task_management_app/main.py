from fastapi import FastAPI
from task_management_app.src.utils.db import Base, engine
from task_management_app.src.tasks.models import TaskModel

print("MAIN FILE RUNNING")

app = FastAPI(title="Task App")

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print(Base.metadata.tables.keys())

