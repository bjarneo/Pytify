#!/usr/bin/python3
from __future__ import absolute_import, unicode_literals
import pytify.pytifylib
from pytify.strategy import get_pytify_class_by_platform
from pytify.song_list import SongList
from pytify.prompt import custom_prompt
from pytify.commander import Commander
import argparse
import sys
import pkg_resources


class App:
    def __init__(self):
        self.pytify = get_pytify_class_by_platform()()

        self.command = Commander(self.pytify)

        self.run()

    def list_songs(self, list):
        SongList(list)

    def run(self):
        parser = argparse.ArgumentParser(description='Spotify remote')

        parser.add_argument(
            '-n', help='for next song', action='store_true'
        )
        parser.add_argument(
            '-p', help='for previous song', action='store_true'
        )
        parser.add_argument(
            '-pp', help='for play and pause song', action='store_true'
        )
        parser.add_argument(
            '-s', help='stop music', action='store_true'
        )
        parser.add_argument(
            '-c', help='current playing', action='store_true'
        )

        args = parser.parse_args()

        if args.n:
            self.pytify.next()

        elif args.p:
            self.pytify.prev()

        elif args.pp:
            self.pytify.play_pause()

        elif args.s:
            self.pytify.stop()

        elif args.c:
            print(self.pytify.get_current_playing())

        else:
            self.interaction()

    def get_package_name(self):
        return pkg_resources.require('pytify')[0]

    def interaction(self):
        print(
            '%s [https://github.com/bjarneo/Pytify]' % self.get_package_name()
        )

        while 1:
            try:
                search_input = custom_prompt(self.pytify.get_current_playing())
            except KeyboardInterrupt:
                continue
            except EOFError:
                print('\n Closing application...\n')
                break

            if self.command.run(search_input):
                continue

            search = self.pytify.query(search_input)

            if search:
                self.list_songs(list=self.pytify.list())


def main():
    App()
