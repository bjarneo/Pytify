#!/usr/bin/env python
from spotipy import spotipy
from spotipy import menu
import argparse
import sys
import curses


class App:
    def __init__(self):
        self.sptfy = spotipy.get_spotipy_class_by_platform()()

        self.run()

    def menu(self, list):
        self.list = list

        curses.wrapper(self.menu_items)

    def menu_items(self, stdscreen):
        curses.curs_set(0)

        main_menu = menu.Menu(self.list, stdscreen)
        main_menu.display()


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
        self.intro()

        while 1:
            if sys.version_info >= (3, 0):
                search_input = input('What artist / song are you searching for?\n> ')
            else:
                search_input = raw_input('What artist / song are you searching for?\n> ')

            if search_input:
                self.sptfy.search(search_input)

                self.menu(list=self.sptfy.list())

# Run the app
if __name__ == '__main__':
    try:
        App()

    except KeyboardInterrupt:
        print('\n Closing application...\n')
