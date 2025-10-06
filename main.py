from fastapi import FastAPI
from routes import tasks

app = FastAPI()

app.include_router(tasks.router,prefix="task",tags=["task"])

@app.get("/")
def health_check():
    return {"status":"ok", "message":"Server is running"}