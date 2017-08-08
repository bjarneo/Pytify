from __future__ import unicode_literals
from pathlib import Path
from prompt_toolkit.history import FileHistory


def history():
    return FileHistory('%s/.pytify-search-history' % str(Path.home()))
