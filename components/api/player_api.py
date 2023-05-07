import asyncio
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from components.database.database import Database


router = APIRouter()
db = Database()

# Odtwarzacz muzyki w pokoju
class MusicPlayer:
    def __init__(self):
        self.playing_clients = set()

    async def play_music(self, websocket: WebSocket, item_id: int):
        item = db.get_playlist_item_by_id(item_id)
        if item:
            # Dodaj klienta do zbioru odtwarzających klientów
            self.playing_clients.add(websocket)

            try:
                # Przekaż strumieniowo dźwięk do wszystkich odtwarzających klientów
                with open(item.path_to_music, "rb") as file:
                    while True:
                        data = file.read(4096)
                        if not data:
                            break
                        await asyncio.gather(
                            *[client.send_bytes(data) for client in self.playing_clients]
                        )
            finally:
                # Usuń klienta z zbioru odtwarzających klientów po zakończeniu odtwarzania
                self.playing_clients.remove(websocket)

# Inicjalizacja odtwarzacza muzyki
player = MusicPlayer()

@router.websocket("/player/{room_id}")
async def player_websocket(websocket: WebSocket, room_id: int):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            if data == "play_next":
                # Pobierz kolejny utwór z playlisty (możesz dostosować logikę, np. na podstawie indeksu)
                next_item = db.get_next_playlist_item()
                if next_item:
                    # Odtwórz muzykę dla wszystkich klientów w pokoju
                    await player.play_music(websocket, next_item.id)
            else:
                await websocket.send_text("Invalid command")
    except WebSocketDisconnect:
        # Jeśli klient rozłączył się, usuń go z odtwarzających klientów
        player.playing_clients.remove(websocket)
        await websocket.close()

