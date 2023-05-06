from fastapi import APIRouter
from pydantic import BaseModel
from components.database.database import Database

router = APIRouter()
db = Database()

class UserCreate(BaseModel):
    nick: str

@router.post("/users")
def create_user(user: UserCreate):
    user_id = db.create_user(user)
    return {"user_id": user_id}

@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = db.get_user_by_id(user_id)
    if user:
        return {"user": user}
    else:
        return {"message": "User not found"}

app = router
