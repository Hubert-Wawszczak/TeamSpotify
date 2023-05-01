from connect import spotify
import json


def search_track(track='', artist='', limit=25):
    if ((track == '') & (artist == '')):
        return
    query = ''
    if (track != ''):
        query += f'track:{track} '
    if (artist != ''):
        query += f'artist:{artist} '

    results = spotify.search(query, type='track', limit=limit)

    counter = 0
    songs = []
    for track in results['tracks']['items']:
        counter += 1
        song = {
            "search_counter": counter,
            "name": track['name'],
            "artists": track['artists'][0]['name'],
            "track_id": track['id'],
            "album_name": track['album']['name'],
            "album_id": track['album']['id'],
            "track_image": track['album']['images'][0]['url']
        }
        songs.append(song)
        track_results = json.dumps(songs)
    return track_results
