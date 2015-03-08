import curses
from curses import panel
from pytifylib import get_pytify_class_by_platform


"""
 TODO: Rewrite this crappy menu class
"""
class Menu(object):
    def __init__(self, items, stdscreen):
        self.pytify = get_pytify_class_by_platform()()
        self.window = stdscreen.subwin(0,0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 2
        self.items = items
        self.song_length = len(items) - 1

        self.items.append(' ')
        self.items.append('<UP> and <DOWN> for navigation.')
        self.items.append('<Enter> to select song.')
        self.items.append('<Esc> for search.')
        self.items.append('<LEFT> and <RIGHT> for prev/next song.')
        self.items.append('<SPACEBAR> for play/pause.')

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
                self.pytify.listen(int(self.position - 1))

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

            elif key == curses.KEY_LEFT:
                self.pytify.prev()

            elif key == curses.KEY_RIGHT:
                self.pytify.next()

            # spacebar
            elif key == 32:
                self.pytify.play_pause()

            # escape
            elif key == 27:
                break

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()
