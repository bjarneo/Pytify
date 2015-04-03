from sys import platform
import subprocess
import requests
import sys


# Fetch songs with spotify api
class Pytifylib:
    # Api url
    url = 'https://api.spotify.com/v1/search?q=%s&type=track,artist'

    # hold songs
    _songs = {}

    # history
    _history = []

    # limit output songs
    _limit = 15

    # Search for song / album / artist
    def search(self, query):
        try:
            search = '+'.join(query.split())
            response = requests.get(self.url % search)

            self._history.append(query)

            self.set_songs(data=response.json())
        except StandardError:
            print('Search went wrong? Please try again.')

    def set_songs(self, data):
        for index, song in enumerate(data['tracks']['items']):
            if index == self._limit:
                break

            if sys.version_info >= (3, 0):
                artist_name = song['artists'][0]['name'][:25]
                song_name = song['name'][:30]
                album_name = song['album']['name'][:30]
            else:
                artist_name = song['artists'][0]['name'][:25].encode('utf-8')
                song_name = song['name'][:30].encode('utf-8')
                album_name = song['album']['name'][:30].encode('utf-8')

            self._songs[index + 1] = {
                'href': song['uri'],
                'artist': artist_name,
                'song': song_name,
                'album': album_name
            }

    def get_songs(self):
        return self._songs

    # List all. Limit if needed
    def list(self):
        list = []
        space = '{0:3} | {1:25} | {2:30} | {3:30}'

        list.append(space.format('#', 'Artist', 'Song', 'Album'))

        # Just to make it pwitty
        list.append(space.format(
            '-' * 3,
            '-' * 25,
            '-' * 30,
            '-' * 30
        ))

        for i in self.get_songs():
            list.append(space.format(
                '%d.' % i,
                '%s' % self.get_songs()[i]['artist'],
                '%s' % self.get_songs()[i]['song'],
                '%s' % self.get_songs()[i]['album']
            ))

        return list

    def _get_song_uri_at_index(self, index):
        return str(self._songs[index]['href'])

    def _get_song_name_at_index(self, index):
        return str('%s - %s' % (self._songs[index]['artist'], self._songs[index]['song']))

    def listen(self, index):
        raise NotImplementedError()

    def print_history(self):
        if len(self._history) > 5:
            self._history.pop(0)

        print('\nLast five search results:')

        for song in self._history:
            print(song)

    def next(self):
        raise NotImplementedError()

    def prev(self):
        raise NotImplementedError()

    def play_pause(self):
        raise NotImplementedError()

    def pause(self):
        raise NotImplementedError()


def get_pytify_class_by_platform():
    if 'linux' in platform:
        return LinuxPytify
    elif 'darwin' in platform:
        return DarwinPytify
    else:
        raise Exception("%s is not supported." % platform)


class DarwinPytify(Pytifylib):
    def __init__(self):
        """
            Check if there is a Spotify process running and if not, run Spotify.
        """
        try:
            count = int(subprocess.check_output([
                "osascript",
                "-e", "tell application \"System Events\"",
                "-e", "count (every process whose name is \"Spotify\")",
                "-e", "end tell"
                ]).strip())
            if count == 0:
                print("\n[OPENING SPOTIFY] The Spotify app was not open.\n")
                self._make_osascript_call("tell application \"Spotify\" to activate")
        except Exception:
            sys.exit("You don't have Spotify installed. Please install it.")

    def _make_osascript_call(self, command):
        subprocess.call([
            'osascript',
            '-e',
            command
        ])

    def listen(self, index):
        uri = self._get_song_uri_at_index(index)
        self._make_osascript_call('tell app "Spotify" to play track "%s"' % uri)

    def next(self):
        self._make_osascript_call('tell app "Spotify" to next track')

    def prev(self):
        self._make_osascript_call('tell app "Spotify" to previous track')

    def play_pause(self):
        self._make_osascript_call('tell app "Spotify" to playpause')

    def pause(self):
        self._make_osascript_call('tell app "Spotify" to pause')


class LinuxPytify(Pytifylib):
    def __init__(self):
        import dbus

        try:
            self.interface = dbus.Interface(
                dbus.SessionBus().get_object(
                    'org.mpris.MediaPlayer2.spotify',
                    '/org/mpris/MediaPlayer2'
                    ), 'org.mpris.MediaPlayer2.Player')

        except dbus.exceptions.DBusException:
            sys.exit('\n Some errors occured. Try restart or start Spotify. \n')

    def listen(self, index):
        uri = self._get_song_uri_at_index(index)
        subprocess.call('spotify %s > /dev/null 2>&1' % uri, shell=True)

    def next(self):
        self.interface.Next()

    def prev(self):
        self.interface.Previous()

    def play_pause(self):
        self.interface.PlayPause()

    def pause(self):
        self.interface.Stop()
