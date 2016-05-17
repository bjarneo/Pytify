from __future__ import unicode_literals
import requests
import sys


# Fetch songs with spotify api
class Pytifylib:
    # Api url
    url = 'https://api.spotify.com/v1/search?q=%s&type=%s'

    # hold songs
    _songs = {}

    # history
    _history = []

    # limit output songs
    _limit = 15

    # query
    def query(self, query):
        try:
            data = self.search(query)

            self._history.append(query)

            self.set_songs(data=data)

            return True
        except Exception as e:
            print(e)

            return False

    # Search for song / album / artist
    def search(self, query, type='track,artist'):
        try:
            search = '+'.join(query.split())

            try:
                response = requests.get(self.url % (search, type))
            except requests.exceptions.RequestException as e:
                print(e)

                sys.exit(1)

            return response.json()
        except StandardError:
            print('Search went wrong? Please try again.')

            return False

    def set_songs(self, data):
        for index, song in enumerate(data['tracks']['items']):
            if index == self._limit:
                break

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
