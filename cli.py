#!/usr/bin/env python
from spotipy import spotipy
import argparse
import sys
import curses
from curses import panel


class Menu(object):
    def __init__(self, items, stdscreen):
        self.sptfy = spotipy.get_spotipy_class_by_platform()()
        self.window = stdscreen.subwin(0,0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 2
        self.items = items
        self.items.append(' ')
        self.items.append('<UP> and <DOWN> to navigate. <Enter> to select song. <Esc> for search.')
        self.items.append('<LEFT> and <RIGHT> for prev/next song. <SPACEBAR> for play/pause.')

    def navigate(self, n):
        self.position += n

        if self.position < 2:
            self.position = 2
        elif self.position > 16:
            self.position = 16
        elif self.position >= len(self.items):
            self.position = len(self.items) - 1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()

            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                self.window.addstr(index, 1, str(item), mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == len(self.items) - 1:
                    break
                else:
                    self.sptfy.listen(int(self.position - 1))

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

            elif key == curses.KEY_LEFT:
                self.sptfy.prev()

            elif key == curses.KEY_RIGHT:
                self.sptfy.next()

            # spacebar
            elif key == 32:
                self.sptfy.play_pause()

            # escape
            elif key == 27:
                break

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()


class App:
    def __init__(self):
        self.sptfy = spotipy.get_spotipy_class_by_platform()()

        self.interaction()

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
