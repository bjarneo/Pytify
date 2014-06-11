import requests
import time
import os


# Fetch songs with spotify api
class Spotify:
    _url = 'https://ws.spotify.com/search/1/track.json?q='

    # Get our data
    def __init__(self, query=False):
        if query:
            response = requests.get(self._url + query)
            self.data = response.json()

    # List all. Limit if needed
    def list(self, limit=100):
        self.songs = {}
        space = '{0:3} | {1:25} | {2:30} | {3:30}'

        print space.format('#', 'Artist', 'Song', 'Album')
        # Just to make it pwitty
        print space.format(
            '---',
            '-------------------------',
            '------------------------------',
            '------------------------------'
        )

        for key, song in enumerate(self.data['tracks']):
            if key == limit:
                break

            print space.format(
                str(key + 1) + '.',
                song['artists'][0]['name'].encode('utf-8'),
                song['name'].encode('utf-8'),
                song['album']['name'].encode('utf-8')
            )

            # Save spotify uri for later use
            self.songs[key + 1] = song['href']

            # Sleep's just for the sexy output
            time.sleep(0.01)

    def listen(self, index):
        os.system('spotify ' + str(self.songs[index]))

    def next(self):
        os.system('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next >/dev/null')

    def prev(self):
        os.system('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous >/dev/null')

    def playPause(self):
        os.system('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause >/dev/null')

    # Debug
    def debug(self):
        print self.data['tracks']
