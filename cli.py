#!/usr/bin/env python
from spotify import spotify
import sys
import os
import dbus


def app():
    sptfy = spotify.Spotify()

    if len(sys.argv) > 1:
        if sys.argv[1] == '-n':
            sptfy.next()

        elif sys.argv[1] == '-p':
            sptfy.prev()

        elif sys.argv[1] == '-pp':
            sptfy.play_pause()

        elif sys.argv[1] == '-s':
            sptfy.stop()

        elif sys.argv[1] == '-m':
            sptfy.meta()

        elif sys.argv[1] == '-h':
            print """
            -n for next song
            -p for previous song
            -pp for pause and play song
            -s to stop song
            """

        else:
            print """
            See -h for help
            """

    else:
        print """
 ############################################################
 #            _____             _   _  __                   #
 #           / ____|           | | (_)/ _|                  #
 #          | (___  _ __   ___ | |_ _| |_ _   _             #
 #           \___ \| '_ \ / _ \| __| |  _| | | |            #
 #           ____) | |_) | (_) | |_| | | | |_| |            #
 #          |_____/| .__/ \___/ \__|_|_|  \__, |            #
 #                 | |                     __/ |            #
 #                 |_|                    |___/             #
 #                                                          #
 # by bjarneo <http://www.github.com/bjarneo/PythonSpotify> #
 #                                                          #
 ############################################################
            """

        while 1:
            search_input = raw_input('What artist / song are you searching for?\n> ')
            if search_input:
                sptfy.search(search_input)
                sptfy.list(15)
                sptfy.print_history()

                song_input = raw_input('\nType song number and press <enter> to play. Press <enter> for new search.\n> ')
                if song_input:
                    print sptfy.listen(int(song_input))
                else:
                    continue

if __name__ == '__main__':
    try:
        app()

    except KeyboardInterrupt:
        print '\n Closing application...\n'

    except dbus.exceptions.DBusException:
        print '\n Start Spotify before using this cli application. \n'
