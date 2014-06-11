#!/usr/bin/env python
import Spotify
import sys


if len(sys.argv) > 1:
    spotify = Spotify.Spotify()

    if sys.argv[1] == '-n':
        spotify.next()

    elif sys.argv[1] == '-p':
        spotify.prev()

    elif sys.argv[1] == '-pp':
        spotify.playPause()

    elif sys.argv[1] == '-h':
        print """
        -n for next song
        -p for previous song
        -pp for pause and play song
        """

    else:
        print """
        See -h for help
        """

else:
    while 1:
        search_input = raw_input('What artist / song are you searching for?\r\n')
        if search_input:
            spotify = Spotify.Spotify(search_input)
            spotify.list(10)

            song_input = raw_input('\r\nType song number and press <enter> to play. Press <enter> for new search.\r\n')
            if song_input:
                spotify.listen(int(song_input))
            else:
                continue