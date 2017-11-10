from __future__ import absolute_import, unicode_literals
import getpass
import os
from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.contrib.completers import WordCompleter
from pytify.history import history


style = style_from_dict({
    Token.Username:  '#84bd00 italic',
    Token.At:        '#999999',
    Token.Host:      '#84bd00',
    Token.Separator: '#84bd00',
    Token.Text:      '#e6e6e6',
    Token.Arrow:     '#999999',
    Token.SelectedText: 'reverse underline',
    Token.Toolbar: '#e6e6e6 bg:#262626',
})


def completer():
    list = []

    for name in history():
        list.append(name)

    return WordCompleter(set(list), ignore_case=True)


def get_bottom_toolbar_tokens(currentSong):
    def toolbar(cli):
        return [
            (Token.Toolbar, ' exit: ctrl+d | clear: ctrl+c | song: %s' % currentSong)
        ]

    return toolbar


def get_prompt_tokens(cli):
    return [
        (Token.Username,  getpass.getuser()),
        (Token.At,        '@'),
        (Token.Host,      os.uname()[1]),
        (Token.Separator, ' - '),
        (Token.Text,      'Search:'),
        (Token.Arrow,     '\n> '),
    ]


def custom_prompt(currentSong):
    return prompt(
        get_prompt_tokens=get_prompt_tokens,
        history=history(),
        auto_suggest=AutoSuggestFromHistory(),
        enable_history_search=True,
        on_abort=AbortAction.RETRY,
        get_bottom_toolbar_tokens=get_bottom_toolbar_tokens(currentSong),
        completer=completer(),
        complete_while_typing=True,
        style=style
    )
