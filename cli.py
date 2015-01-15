#!/usr/bin/env python
from spotipy import spotipy
import dbus
import argparse
import sys


def app():
    sptfy = spotipy.Spotipy()

    parser = argparse.ArgumentParser(description='Spotify controller')

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
        print("""
 ################################################################
 #                                                              #
 #      ____                    __                              #
 #     /\  _`\                 /\ \__  __                       #
 #     \ \,\L\_\  _____     ___\ \ ,_\/\_\  _____   __  __      #
 #      \/_\__ \ /\ '__`\  / __`\ \ \/\/\ \/\ '__`\/\ \/\ \     #
 #        /\ \L\ \ \ \L\ \/\ \L\ \ \ \_\ \ \ \ \L\ \ \ \_\ \    #
 #        \ `\____\ \ ,__/\ \____/\ \__\\ \_\ \ ,__/\/`____  \   #
 #         \/_____/\ \ \/  \/___/  \/__/ \/_/\ \ \/  `/___/> \  #
 #                  \ \_\                     \ \_\     /\___/  #
 #                   \/_/                      \/_/     \/__/   #
 #                                                              #
 #                                                              #
 #    by bjarneo <http://www.github.com/bjarneo/Spotipy>        #
 #                                                              #
 ################################################################
            """)

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
                else:
                    continue

if __name__ == '__main__':
    try:
        app()

    except KeyboardInterrupt:
        print('\n Closing application...\n')
