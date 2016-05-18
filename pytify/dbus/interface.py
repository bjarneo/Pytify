from __future__ import absolute_import, unicode_literals
import dbus


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
                '\n Some errors occured. Try restart or start Spotify. \n'
            )

        return interface
    factory = staticmethod(factory)
