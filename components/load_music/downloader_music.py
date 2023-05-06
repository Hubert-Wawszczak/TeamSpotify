from fastapi import APIRouter
from pydantic import BaseModel
import yt_dlp
import os

router = APIRouter()

class SearchQuery(BaseModel):
    query: str

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': r'C:\Users\Hubert\Downloads\ffmpeg-2023-05-04-git-4006c71d19-full_build\bin',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@router.post("/search")
def search_youtube(query: SearchQuery):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'extract_flat': 'in_playlist',
        'forcejson': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch:{query.query}", download=False)
        if 'entries' in search_results:
            results = []
            for entry in search_results['entries']:
                results.append({
                    'title': entry['title'],
                    'url': entry['webpage_url']
                })
            return results
        else:
            return []







@router.post("/download")
def download_from_youtube(query: SearchQuery):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    download_dir = os.path.join(base_dir, "../../temp/downloaded_music")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': r'C:\Users\Hubert\Downloads\ffmpeg-2023-05-04-git-4006c71d19-full_build\bin',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch:{query.query}", download=False)
        if 'entries' in search_results and len(search_results['entries']) > 0:
            url = search_results['entries'][0]['webpage_url']
            ydl.download([url])
            return {"message": "Pobrano audio z YouTube."}
        else:
            return {"message": "Brak wyników wyszukiwania lub nie można pobrać URL."}



app = router