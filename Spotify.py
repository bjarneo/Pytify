import requests
import time
import os
import dbus
# Fetch songs with spotify api
class Spotify:
    _url = 'https://ws.spotify.com/search/1/track.json?q='

    # Get our data
    def __init__(self):
        self.__songs = {}
        self.__history = []
        self.__data = ''

        session_bus = dbus.SessionBus()
        self.spotify = dbus.Interface(
            session_bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2'),
            'org.mpris.MediaPlayer2.Player'
        )

    def search(self, query):
        if query:
            response = requests.get(self._url + query)
            self.__data = response.json()
            self.__history.append(query)

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

        for key, song in enumerate(self.__data['tracks']):
            if key == limit:
                break

            print space.format(
                str(key + 1) + '.',
                song['artists'][0]['name'].encode('utf-8'),
                song['name'].encode('utf-8'),
                song['album']['name'].encode('utf-8')
            )

            # Save spotify uri and song for later use
            self.__songs[key + 1] = {
                'href': song['href'],
                'song': '%s - %s' % (song['artists'][0]['name'].encode('utf-8'), song['name'].encode('utf-8'))
            }

            # Sleep's just for the sexy output
            time.sleep(0.01)

    def listen(self, index):
        os.system('spotify ' + str(self.__songs[index]['href']) + ' > /dev/null 2>&1')

        return '\nPlaying: %s\n' % str(self.__songs[index]['song'])

    def print_history(self):
        if len(self.__history) > 5:
            self.__history.pop(0)

        print '\nLast five search results:'
        for song in self.__history:
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
        print self.__data['tracks']