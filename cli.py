#!/usr/bin/env python
from spotipy import spotipy
import argparse
import sys


class App:
    def __init__(self):
        self.sptfy = spotipy.get_spotipy_class_by_platform()()

        self.run()

    def run(self):
        parser = argparse.ArgumentParser(description='Spotify remote')

        parser.add_argument('-n', help='for next song', action='store_true')
        parser.add_argument('-p', help='for previous song', action='store_true')
        parser.add_argument('-pp', help='for play and pause song', action='store_true')
        parser.add_argument('-s', help='stop music', action='store_true')

        args = parser.parse_args()

        if args.n:
            self.sptfy.next()

        elif args.p:
            self.sptfy.prev()

        elif args.pp:
            self.sptfy.play_pause()

        elif args.s:
            self.sptfy.stop()

        else:
            self.intro()

            self.interaction()

    def intro(self):
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

    def interaction(self):
        while 1:
            if sys.version_info >= (3, 0):
                search_input = input('What artist / song are you searching for?\n> ')
            else:
                search_input = raw_input('What artist / song are you searching for?\n> ')

            if search_input:
                self.sptfy.search(search_input)
                self.sptfy.list(15)
                self.sptfy.print_history()

                if sys.version_info >= (3, 0):
                    song_input = input('\nType song number and press <enter> to play. Press <enter> for new search.\n> ')
                else:
                    song_input = raw_input('\nType song number and press <enter> to play. Press <enter> for new search.\n> ')

                if song_input:
                    try:
                        self.sptfy.listen(int(song_input))
                    # stop user entering something that is not a number.
                    except ValueError:
                        continue



# Run the app
if __name__ == '__main__':
    try:
        App()

    except KeyboardInterrupt:
        print('\n Closing application...\n')
