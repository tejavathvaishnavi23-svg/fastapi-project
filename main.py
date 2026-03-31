from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Vaishnavi, FastAPI is working!"}

@app.get("/about")
def about():
    return {"info": "This is about page"}