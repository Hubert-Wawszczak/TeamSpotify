from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from components.database.database import Database

router = APIRouter()
db = Database()


class RoomCreate(BaseModel):
    nazwa: str
    haslo: str


class RoomUpdate(BaseModel):
    nazwa: str
    haslo: str


@router.get("/rooms/{room_id}")
def get_room(room_id: int):
    room = db.get_room_by_id(room_id)
    if room:
        return {"room": room}
    else:
        raise HTTPException(status_code=404, detail="Room not found")


@router.post("/rooms")
def create_room(room: RoomCreate):
    existing_room = db.get_room_by_name(room.nazwa)
    if existing_room:
        raise HTTPException(status_code=409, detail="Room already exists")

    room_id = db.create_room(room)
    return {"room_id": room_id}


@router.put("/rooms/{room_id}")
def update_room(room_id: int, room: RoomUpdate):
    existing_room = db.get_room_by_id(room_id)
    if not existing_room:
        raise HTTPException(status_code=404, detail="Room not found")

    db.update_room(room_id, room)
    return {"message": "Room updated"}


@router.delete("/rooms/{room_id}")
def delete_room(room_id: int):
    existing_room = db.get_room_by_id(room_id)
    if not existing_room:
        raise HTTPException(status_code=404, detail="Room not found")

    db.delete_room(room_id)
    return {"message": "Room deleted"}
