import requests
import time
import os
import dbus


# Fetch songs with spotify api
class Spotify:
    url = 'https://ws.spotify.com/search/1/track.json?q='

    # Get our data
    def __init__(self):
        self._songs = {}
        self._history = []
        self._data = None 
        self.spotify = dbus.Interface(
            dbus.SessionBus().get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2'),
            'org.mpris.MediaPlayer2.Player'
        )

    def search(self, query):
        try:
            response = requests.get(self.url + query)
            self._data = response.json()
            self._history.append(query)
        except StandardError:
            print 'Search went wrong? Please try again.'

    # List all. Limit if needed
    def list(self, limit=100):
        space = '{0:3} | {1:25} | {2:30} | {3:30}'

        print space.format('#', 'Artist', 'Song', 'Album')
        # Just to make it pwitty
        print space.format(
            '-' * 3,
            '-' * 25,
            '-' * 30,
            '-' * 30
        )

        for key, song in enumerate(self._data['tracks']):
            if key == limit:
                break

            print space.format(
                str(key + 1) + '.',
                song['artists'][0]['name'][:25].encode('utf-8'),
                song['name'][:30].encode('utf-8'),
                song['album']['name'][:30].encode('utf-8')
            )

            # Save spotify uri and song for later use
            self._songs[key + 1] = {
                'href': song['href'],
                'song': '%s - %s' % (song['artists'][0]['name'].encode('utf-8'), song['name'].encode('utf-8'))
            }

            # Sleep's just for the sexy output
            time.sleep(0.01)

    def listen(self, index):
        os.system('spotify %s > /dev/null 2>&1' % str(self._songs[index]['href']))

        return '\nPlaying: %s \n' % str(self._songs[index]['song'])

    def print_history(self):
        if len(self._history) > 5:
            self._history.pop(0)

        print '\nLast five search results:'
        for song in self._history:
            print song

    def next(self):
        self.spotify.Next()

    def prev(self):
        self.spotify.Prev()

    def play_pause(self):
        self.spotify.PlayPause()

    def stop(self):
        self.spotify.Stop()

    def meta(self):
        # TODO: Fix metadata output
        os.system('dbus-send --print-reply --session --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:"org.mpris.MediaPlayer2.Player" string:"Metadata"')

    # Debug
    def debug(self):
        print self._data['tracks']
