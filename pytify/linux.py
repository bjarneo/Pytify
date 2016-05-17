from __future__ import absolute_import, unicode_literals
import sys
import dbus
from pytify.pytifylib import Pytifylib
from pytify.dbus.metadata import Metadata


class Linux(Pytifylib):
    def __init__(self):
        try:
            self.interface = dbus.Interface(
                dbus.SessionBus().get_object(
                    'org.mpris.MediaPlayer2.spotify',
                    '/org/mpris/MediaPlayer2'
                ),
                'org.mpris.MediaPlayer2.Player'
            )

            self.metadata = Metadata()

        except dbus.exceptions.DBusException:
            sys.exit('\n Some errors occured. Try restart or start Spotify. \n')

    def listen(self, index):
        self.interface.OpenUri(
            self._get_song_uri_at_index(index)
        )

    def next(self):
        self.interface.Next()

    def prev(self):
        self.interface.Previous()

    def play_pause(self):
        self.interface.PlayPause()

    def pause(self):
        self.interface.Stop()

    def get_current_playing(self):
        return self.metadata.get_current_playing()
