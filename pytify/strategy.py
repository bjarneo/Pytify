from sys import platform

def get_pytify_class_by_platform():
    if 'linux' in platform:
        from linux import Linux

        return Linux
    elif 'darwin' in platform:
        from darwin import Darwin

        return Darwin
    else:
        raise Exception('%s is not supported.' % platform)
