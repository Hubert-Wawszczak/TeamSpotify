from fastapi import FastAPI
from components.api.user_api import router as user_router
from components.load_music.downloader_music import app as downloader_app
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/users")
app.include_router(downloader_app, prefix="/downloader")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
