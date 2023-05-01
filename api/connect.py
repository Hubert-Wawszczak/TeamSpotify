import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

cid = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
scope = os.getenv("SCOPE")


def spotify_connect():
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
                                                        client_secret=secret,
                                                        redirect_uri=redirect_uri,
                                                        scope=scope))
    return spotify


spotify = spotify_connect()
