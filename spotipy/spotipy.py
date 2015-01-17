from sys import platform
import subprocess
import requests
import time
import sys


# Fetch songs with spotify api
class Spotipy:
    # Api url
    url = 'https://ws.spotify.com/search/1/track.json?q='

    # hold songs
    _songs = {}

    # history
    _history = []

    # data
    _data = None

    # Get our data
    def __init__(self):
        if 'linux' in platform:
            import dbus

            try:
                self.interface = dbus.Interface(
                    dbus.SessionBus().get_object(
                        'org.mpris.MediaPlayer2.spotify',
                        '/org/mpris/MediaPlayer2'
                        ),
                        'org.mpris.MediaPlayer2.Player'
                    )

            except dbus.exceptions.DBusException:
                sys.exit('\n Some errors occured. Try restart or start Spotify. \n')

    def search(self, query):
        try:
            response = requests.get(self.url + query)

            self._data = response.json()

            self._history.append(query)
        except StandardError:
            print('Search went wrong? Please try again.')

    # List all. Limit if needed
    def list(self, limit=100):
        space = '{0:3} | {1:25} | {2:30} | {3:30}'

        print(space.format('#', 'Artist', 'Song', 'Album'))

        # Just to make it pwitty
        print(space.format(
            '-' * 3,
            '-' * 25,
            '-' * 30,
            '-' * 30
        ))

        for index, song in enumerate(self._data['tracks']):
            if index == limit:
                break

            if sys.version_info >= (3, 0):
                artist_name = song['artists'][0]['name'][:25]
                song_name = song['name'][:30]
                album_name = song['album']['name'][:30]
            else:
                artist_name = song['artists'][0]['name'][:25].encode('utf-8')
                song_name = song['name'][:30].encode('utf-8')
                album_name = song['album']['name'][:30].encode('utf-8')

            print(space.format(
                '%d.' % (index + 1),
                '%s' % artist_name,
                '%s' % song_name,
                '%s' % album_name
            ))

            # Save spotify uri and song for later use
            self._songs[index + 1] = {
                'href': song['href'],
                'song': '%s - %s' % (artist_name, song_name )
            }

            # Sleep's just for the sexy output
            time.sleep(0.01)

    def listen(self, index):
        uri = str(self._songs[index]['href'])

        if 'linux' in platform:
            subprocess.call('spotify %s > /dev/null 2>&1' % uri, shell=True)
        elif 'darwin' in platform:
            subprocess.call([
                'osascript',
                '-e',
                'tell app \'Spotify\' to play track \'%s\'' % uri
            ])

        print('\nPlaying: %s \n' % str(self._songs[index]['song']))

    def print_history(self):
        if len(self._history) > 5:
            self._history.pop(0)

        print('\nLast five search results:')

        for song in self._history:
            print(song)

    def next(self):
        if 'linux' in platform:
            self.interface.Next()
        elif 'darwin' in platform:
            subprocess.call([
                'osascript',
                '-e',
                'tell app \'Spotify\' to next track'
            ])

    def prev(self):
        if 'linux' in platform:
            self.interface.Prev()
        elif 'darwin' in platform:
            subprocess.call([
                'osascript',
                '-e',
                'tell app \'Spotify\' to previous track'
            ])

    def play_pause(self):
        if 'linux' in platform:
            self.interface.PlayPause()
        elif 'darwin' in platform:
            subprocess.call([
                'osascript',
                '-e',
                'tell app \'Spotify\' to playpause'
            ])

    def pause(self):
        if 'linux' in platform:
            self.interface.Stop()
        elif 'darwin' in platform:
            subprocess.call([
                'osascript',
                '-e',
                'tell app \'Spotify\' to pause'
            ])
