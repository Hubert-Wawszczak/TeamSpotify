from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from components.database.database import Database


router = APIRouter()
db = Database()


class PlaylistItem(BaseModel):
    path_to_music: str


@router.get("/playlist/{item_id}")
def get_playlist_item(item_id: int):
    item = db.get_playlist_item_by_id(item_id)
    if item:
        return {"item": item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@router.post("/playlist")
def create_playlist_item(item: PlaylistItem):
    item_id = db.create_playlist_item(item)
    return {"item_id": item_id}


@router.put("/playlist/{item_id}")
def update_playlist_item(item_id: int, item: PlaylistItem):
    existing_item = db.get_playlist_item_by_id(item_id)
    if existing_item:
        db.update_playlist_item(item_id, item)
        return {"message": "Item updated"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/playlist/{item_id}")
def delete_playlist_item(item_id: int):
    existing_item = db.get_playlist_item_by_id(item_id)
    if existing_item:
        db.delete_playlist_item(item_id)
        return {"message": "Item deleted"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")



