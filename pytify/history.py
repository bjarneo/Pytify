from __future__ import unicode_literals
from prompt_toolkit.history import FileHistory


def history():
    return FileHistory('.pytify-search-history')
