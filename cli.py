#!/usr/bin/env python
from spotipy import spotipy
import argparse
import sys


def intro():
    print(' ################################################################')
    print(' #                                                              #')
    print(' #      ____                    __                              #')
    print(' #     /\  _`\                 /\ \__  __                       #')
    print(' #     \ \,\L\_\  _____     ___\ \ ,_\/\_\  _____   __  __      #')
    print(' #      \/_\__ \ /\ \'__`\  / __`\ \ \/\/\ \/\ \'__`\/\ \/\ \     #')
    print(' #        /\ \L\ \ \ \L\ \/\ \L\ \ \ \_\ \ \ \ \L\ \ \ \_\ \    #')
    print(' #        \ `\____\ \ ,__/\ \____/\ \__\\ \_\ \ ,__/\/`____  \   #')
    print(' #         \/_____/\ \ \/  \/___/  \/__/ \/_/\ \ \/  `/___/> \  #')
    print(' #                  \ \_\                     \ \_\     /\___/  #')
    print(' #                   \/_/                      \/_/     \/__/   #')
    print(' #                                                              #')
    print(' #                                                              #')
    print(' #    by bjarneo <http://www.github.com/bjarneo/Spotipy>        #')
    print(' #                                                              #')
    print(' ################################################################')

def app():
    sptfy = spotipy.Spotipy()

    parser = argparse.ArgumentParser(description='Spotify remote')

    parser.add_argument('-n', help='for next song', action='store_true')
    parser.add_argument('-p', help='for previous song', action='store_true')
    parser.add_argument('-pp', help='for play and pause song', action='store_true')
    parser.add_argument('-s', help='stop music', action='store_true')

    args = parser.parse_args()

    if args.n:
        sptfy.next()

    elif args.p:
        sptfy.prev()

    elif args.pp:
        sptfy.play_pause()

    elif args.s:
        sptfy.stop()

    else:
        intro()

        # Our interaction
        while 1:
            if sys.version_info >= (3, 0):
                search_input = input('What artist / song are you searching for?\n> ')
            else:
                search_input = raw_input('What artist / song are you searching for?\n> ')

            if search_input:
                sptfy.search(search_input)
                sptfy.list(15)
                sptfy.print_history()

                if sys.version_info >= (3, 0):
                    song_input = input('\nType song number and press <enter> to play. Press <enter> for new search.\n> ')
                else:
                    song_input = raw_input('\nType song number and press <enter> to play. Press <enter> for new search.\n> ')

                if song_input:
                    sptfy.listen(int(song_input))

# Run the app
if __name__ == '__main__':
    try:
        app()

    except KeyboardInterrupt:
        print('\n Closing application...\n')
