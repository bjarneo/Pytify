#!/usr//bin/env python
import Spotify


search_input = raw_input('What artist / song are you searching for?\r\n')

if search_input:
    spotify = Spotify.Spotify(search_input)
    spotify.list(10)

    song_input = raw_input('\r\nType song number and hit enter to start song.\r\n')
    if song_input:
        spotify.listen(int(song_input))

else:
    print """
    You need to add an argument.
    """