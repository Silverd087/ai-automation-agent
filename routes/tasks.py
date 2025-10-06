from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_task():
    return {"message":"task completed"}