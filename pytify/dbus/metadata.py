from __future__ import absolute_import, unicode_literals
from pytify.dbus.interface import Interface


class Metadata():
    def __init__(self):
        self.interface = Interface.factory('org.freedesktop.DBus.Properties')

    def get_metadata(self):
        return self.interface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

    def get_current_playing(self):
        playing = {}

        for key, value in self.get_metadata().items():
            if key == 'xesam:album':
                playing['album'] = value

            elif key == 'xesam:title':
                playing['title'] = value

            elif key == 'xesam:artist':
                playing['artist'] = value[0]

        return '%s - %s [%s]' % (playing['artist'],
                                 playing['title'],
                                 playing['album'])
