#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals
import pytify.pytifylib
from pytify.strategy import get_pytify_class_by_platform
from pytify.menu import Menu
from pytify.prompt import custom_prompt
import argparse
import sys
import curses
import pkg_resources


class App:
    def __init__(self):
        self.pytify = get_pytify_class_by_platform()()

        self.run()

    def menu(self, list):
        self.list = list

        curses.wrapper(self.menu_items)

    def menu_items(self, stdscreen):
        curses.curs_set(0)

        main_menu = Menu(self.list, stdscreen)
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

    def get_package_name(self):
        return pkg_resources.require('pytify')[0]

    def interaction(self):
        print('%s [https://github.com/bjarneo/Pytify]' % self.get_package_name())

        while 1:
            search_input = custom_prompt()

            search = self.pytify.query(search_input)

            if search is not False:
                self.menu(list=self.pytify.list())

def main():
    try:
        App()
    except EOFError:
        print('\n Closing application...\n')
    except KeyboardInterrupt:
        print('\n Closing application...\n')
