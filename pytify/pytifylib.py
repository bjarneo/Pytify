from __future__ import unicode_literals
import sys
import spotipy
from pytify.history import history
from spotipy.oauth2 import SpotifyClientCredentials


# Fetch songs with spotify api
class Pytifylib:
    # hold songs
    _songs = {}

    # limit output songs
    _limit = 15

    def _spotify(self):
        return self.getCredentials()

    def getCredentials(self):
        try:
            return spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        except spotipy.oauth2.SpotifyOauthError:
            print('Did not find Spotify credentials.')

            print('Please visit https://github.com/bjarneo/pytify#credentials for more information.')

            sys.exit(1)

    # query
    def query(self, query):
        try:
            data = self.search(query)

            self.set_songs(data=data)

            return True
        except Exception as e:
            print(e)

            return False

    # Search for song / artist
    def search(self, query, type='artist,track'):
        try:
            response = self._spotify().search(q='+'.join(query.split()), type=type, limit=self._limit)

        except spotipy.client.SpotifyException:
            print('Search went wrong? Please try again.')

            return False

        return response

    def set_songs(self, data):
        for index, song in enumerate(data['tracks']['items']):
            artist_name = song['artists'][0]['name'][:25]
            song_name = song['name'][:30]
            album_name = song['album']['name'][:30]

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

        for key, song in self.get_songs().items():
            list.append(space.format(
                '%d.' % key,
                '%s' % song['artist'],
                '%s' % song['song'],
                '%s' % song['album']
            ))

        return list

    def _get_song_uri_at_index(self, index):
        return str(self._songs[index]['href'])

    def _get_song_name_at_index(self, index):
        return str(
            '%s - %s' % (self._songs[index]['artist'],
                         self._songs[index]['song'])
        )

    def print_history(self):
        print('\nLast ten entries from history:')

        entries = history().load_history_strings()
        entries = list(entries)

        qty = len(entries)

        for entry in entries[qty-10:qty]:
            print(entry)

    def listen(self, index):
        raise NotImplementedError()

    def next(self):
        raise NotImplementedError()

    def prev(self):
        raise NotImplementedError()

    def play_pause(self):
        raise NotImplementedError()

    def pause(self):
        raise NotImplementedError()

    def get_current_playing(self):
        return ''
