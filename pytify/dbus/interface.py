from __future__ import absolute_import, unicode_literals
import dbus
import sys


class Interface():
    def factory(type):
        try:
            interface = dbus.Interface(
                dbus.SessionBus().get_object(
                    'org.mpris.MediaPlayer2.spotify',
                    '/org/mpris/MediaPlayer2'
                ),
                type
            )
        except dbus.exceptions.DBusException:
            """
                If we catch this exception, Spotify is not running.
                Let the user know.
            """
            sys.exit(
                "\nSome errors occured. Try restart or start Spotify. Pytify is just a cli application which controls Spotify. So you can't use Pytify without Spotify.\n"
            )

        return interface
    factory = staticmethod(factory)
