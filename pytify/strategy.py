from sys import platform
from linuxpytify import LinuxPytify
from darwinpytify import DarwinPytify


def get_pytify_class_by_platform():
    if 'linux' in platform:
        return LinuxPytify
    elif 'darwin' in platform:
        return DarwinPytify
    else:
        raise Exception('%s is not supported.' % platform)
