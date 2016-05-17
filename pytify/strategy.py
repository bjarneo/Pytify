from __future__ import absolute_import, unicode_literals
from sys import platform


def get_pytify_class_by_platform():
    if 'linux' in platform:
        from pytify.linux import Linux

        return Linux
    elif 'darwin' in platform:
        from pytify.darwin import Darwin

        return Darwin
    else:
        raise Exception('%s is not supported.' % platform)
