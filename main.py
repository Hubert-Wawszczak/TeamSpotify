from fastapi import FastAPI
from components.api.user_api import router as user_router
from components.load_music.downloader_music import router as downloader_app
from components.api.room_api import router as room_router
from components.api.playlist_api import router as playlist_router
from components.api.player_api import router as player_router
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/users")
app.include_router(downloader_app, prefix="/downloader")
app.include_router(room_router, prefix="/rooms")
app.include_router(playlist_router, prefix="/playlist")
app.include_router(player_router, prefix="/player")




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
