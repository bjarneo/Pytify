from sys import platform

def get_pytify_class_by_platform():
    if 'linux' in platform:
        from linuxpytify import LinuxPytify

        return LinuxPytify
    elif 'darwin' in platform:
        from darwinpytify import DarwinPytify

        return DarwinPytify
    else:
        raise Exception('%s is not supported.' % platform)
