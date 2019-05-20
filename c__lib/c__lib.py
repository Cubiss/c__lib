import sys


class CubissException(Exception):
    """Base exception for cubiss module."""
    pass


def get_platform():
    """Returns 'lin' on linux, 'win' on windows or 'osx' on mac."""
    platforms = {
        'linux1': 'lin',
        'linux2': 'lin',
        'darwin': 'osx',
        'win32': 'win'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


if __name__ == '__main__':
    print('This is just a library. Not a runnable script.')
