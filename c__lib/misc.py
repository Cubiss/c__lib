import sys
import os
import tempfile
try:
    import win32file
except ImportError:
    win32file = None


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


def link(target, link_name, overwrite=False, try_symlink=False, try_junction=True):
    """
    Create a link named link_name pointing to target.
    If try_link is set and link creation fails, try to create symlink.
    If the try_junction is set, try to create junction.
    If link_name exists then FileExistsError is raised, unless overwrite=True.
    When trying to overwrite a directory, IsADirectoryError is raised.
    """

    if not overwrite:
        try:
            os.link(target, link_name)
        except OSError:
            if try_junction and os.path.isdir(target):
                win32file.CreateSymbolicLink(link_name, target, 1)
            elif try_symlink:
                os.symlink(target, link_name)
            else:
                raise
        return

    # os.replace() may fail if files are on different filesystems
    link_dir = os.path.dirname(link_name)

    # Create link to target with temporary filename
    while True:
        temp_link_name = tempfile.mktemp(dir=link_dir)

        # os.* functions mimic as closely as possible system functions
        # The POSIX symlink() returns EEXIST if link_name already exists
        # https://pubs.opengroup.org/onlinepubs/9699919799/functions/symlink.html
        try:
            try:
                os.link(target, link_name)
            except OSError:
                if try_junction and os.path.isdir(target):
                    win32file.CreateSymbolicLink(link_name, target, 1)
                elif try_symlink:
                    os.symlink(target, link_name)
                else:
                    raise
            break
        except FileExistsError:
            pass

    # Replace link_name with temp_link_name
    try:
        # Pre-empt os.replace on a directory with a nicer message
        if os.path.isdir(link_name):
            raise IsADirectoryError(f"Cannot symlink over existing directory: '{link_name}'")
        os.replace(temp_link_name, link_name)
    except:
        if os.path.islink(temp_link_name):
            os.remove(temp_link_name)
        raise


if __name__ == '__main__':
    print('This is just a library. Not a runnable script.')
