#!/usr/bin/env python
import pytifylib
import menu
import argparse
import sys
import curses


class App:
    def __init__(self):
        self.pytify = pytifylib.get_pytify_class_by_platform()()

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
            self.pytify.next()

        elif args.p:
            self.pytify.prev()

        elif args.pp:
            self.pytify.play_pause()

        elif args.s:
            self.pytify.stop()

        else:
            self.interaction()

    def intro(self):
        print('################################################')
        print('#         ____ _  _ ____ __ ____ _  _          #')
        print('#        (  _ ( \/ (_  _(  (  __( \/ )         #')
        print('#         ) __/)  /  )(  )( ) _) )  /          #')
        print('#        (__) (__/  (__)(__(__) (__/           #')
        print('#                 by bjarneo                   #')
        print('#    <http://www.github.com/bjarneo/Pytify>    #')
        print('################################################')

    def interaction(self):
        self.intro()

        while 1:
            if sys.version_info >= (3, 0):
                search_input = input('What artist / song are you searching for?\n> ')
            else:
                search_input = raw_input('What artist / song are you searching for?\n> ')

            if search_input:
                self.pytify.search(search_input)

                self.menu(list=self.pytify.list())


def main():
    try:
        App()

    except KeyboardInterrupt:
        print('\n Closing application...\n')
