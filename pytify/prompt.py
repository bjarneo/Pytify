from __future__ import absolute_import, unicode_literals
import getpass
import os
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter, ThreadedCompleter
from pytify.history import history

style = Style.from_dict({
    'username':  '#84bd00 italic',
    'at':        '#999999',
    'host':      '#84bd00',
    'separator': '#84bd00',
    'text':      '#e6e6e6',
    'arrow':     '#999999',
    'selectedtext': 'reverse underline',
    'toolbar': '#e6e6e6 bg:#262626',
})


def completer():
    s = set()

    history_strings = history().load_history_strings()

    for name in history_strings:
        s.add(name)

    return WordCompleter(list(s), ignore_case=True)


def get_bottom_toolbar(currentSong):
    def toolbar():
        return [
            ('class:toolbar', ' exit: ctrl+d | clear: ctrl+c | song: %s' % currentSong)
        ]

    return toolbar


def get_prompt():
    return [
        ('class:username',  getpass.getuser()),
        ('class:at',        '@'),
        ('class:host',      os.uname()[1]),
        ('class:seperator', ' - '),
        ('class:text',      'Search:'),
        ('class:arrow',     '\n> '),
    ]


def custom_prompt(currentSong): 
    
    session = PromptSession(
        message=get_prompt,
        history=history(),
        auto_suggest=AutoSuggestFromHistory(),
        enable_history_search=True,
        bottom_toolbar=get_bottom_toolbar(currentSong),
        completer=completer(),
        complete_while_typing=True,
        complete_in_thread=True,
        style=style
    )

    return session.prompt()

