from __future__ import absolute_import, unicode_literals
import sys
import subprocess
from pytify.pytifylib import Pytifylib


class Darwin(Pytifylib):
    def __init__(self):
        """
            Check if there is a Spotify process running and if not,
            run Spotify.
        """
        try:
            count = int(subprocess.check_output([
                    'osascript',
                    '-e', 'tell application "System Events"',
                    '-e', 'count (every process whose name is "Spotify")',
                    '-e', 'end tell'
                ]).strip())
            if count == 0:
                print('\n[OPENING SPOTIFY] The Spotify app was not open.\n')

                self._make_osascript_call(
                    'tell application "Spotify" to activate'
                )
        except Exception:
            sys.exit('You don\'t have Spotify installed. Please install it.')

    def _make_osascript_call(self, command):
        subprocess.call([
            'osascript',
            '-e',
            command
        ])

    def listen(self, index):
        uri = self._get_song_uri_at_index(index)
        self._make_osascript_call(
            'tell app "Spotify" to play track "%s"' % uri
        )

    def next(self):
        self._make_osascript_call('tell app "Spotify" to next track')

    def prev(self):
        self._make_osascript_call('tell app "Spotify" to previous track')

    def play_pause(self):
        self._make_osascript_call('tell app "Spotify" to playpause')

    def pause(self):
        self._make_osascript_call('tell app "Spotify" to pause')

    def get_current_playing(self):
        instruction = ('on getCurrentTrack()\n'
            ' tell application "Spotify"\n'
            '  set currentArtist to artist of current track as string\n'
            '  set currentTitle to name of current track as string\n'
            '  return currentArtist & " - " & currentTitle\n'
            ' end tell\n'
            'end getCurrentTrack\n'
            'getCurrentTrack()')
        proc = subprocess.Popen(
            ['osascript', '-e', instruction],
            stdout=subprocess.PIPE)
        out, err = proc.communicate()
        return out.decode(sys.getfilesystemencoding())
