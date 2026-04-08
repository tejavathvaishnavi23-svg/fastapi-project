from fastapi import FastAPI
from src.tasks.router import task_routes

app = FastAPI(title="Task App")
app.include_router(task_routes)

