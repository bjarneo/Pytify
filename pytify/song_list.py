from __future__ import absolute_import, unicode_literals
import curses, sys
from curses import panel
from pytify.strategy import get_pytify_class_by_platform


class SongList():
    def __init__(self, items):
        self.pytify = get_pytify_class_by_platform()()
        self.items = items

        self.position = 2
        self.song_length = len(items) - 1

        # Init curses screen
        self.window = curses.initscr()

        self.window.keypad(1)

        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        # Show shortcuts
        self.shortcuts()

        # Disable echoing of keys to the screen
        curses.noecho()

        # Disable blinking cursor
        curses.curs_set(False)

        # Use user terminal settings
        curses.endwin()

        # Display window
        self.display()

    def shortcuts(self):
        self.items.append(' ')
        self.items.append('Keyboard shortcuts')
        self.items.append('==================')
        self.items.append('Navigation:')
        self.items.append('  <k> <up> ')
        self.items.append('  <j> <down> ')
        self.items.append('Prev: <h> <left>')
        self.items.append('Next: <l> <right>')
        self.items.append('Play: <p> <enter>')
        self.items.append('Search: <s>')
        self.items.append('Play/Pause: <spacebar>')
        self.items.append('Quit: <q>')

    def navigate(self, n):
        self.position += n

        if self.position < 2:
            self.position = 2
        elif self.position > self.song_length:
            self.position = self.song_length

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        # Play keys.
        play = lambda c: c == ord('p') or c == curses.KEY_ENTER or c == 10 or c == 13

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

            # Start song
            if play(key):
                self.pytify.listen(int(self.position - 1))

            # Up
            elif key == ord('k') or key == curses.KEY_UP:
                self.navigate(-1)

            # Down
            elif key == ord('j') or key == curses.KEY_DOWN:
                self.navigate(1)

            # Left
            elif key == ord('h') or key == curses.KEY_LEFT:
                self.pytify.prev()

            # Rights
            elif key == ord('l') or key == curses.KEY_RIGHT:
                self.pytify.next()

            # Play/Pause
            elif key == ord(' '):
                self.pytify.play_pause()

            # Search
            elif key == ord('s'):
                break

            # Search
            elif key == ord('q'):
                curses.endwin()
                sys.exit()


        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()
