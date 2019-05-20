# version 1.0.0
from c__lib.c__lib import get_platform, CubissException

# Getting implementations based on system.
try:
    if get_platform() == 'win':
        # readline implementation does not work on windows
        raise ImportError()
    import readline
    c__input_implementation = 'linux'
except ImportError:
    try:
        from pyreadline import Readline

        readline = Readline()

        c__input_implementation = 'windows'
    except ImportError:
        c__input_implementation = False

# c__input
if c__input_implementation == 'linux':
    def c__input(prompt, prefill=''):
        readline.set_startup_hook(lambda: readline.insert_text(prefill))
        try:
            return input(prompt)
        finally:
            readline.set_startup_hook()
elif c__input_implementation == 'windows':

    print('Using {} implementation.'.format(c__input_implementation))

    def asd():
        print('asd was called.')

    def c__input(prompt, prefill=''):
        # lambda: readline.insert_text(prefill)
        readline.set_pre_input_hook(asd)
        try:
            return input(prompt)
        finally:
            readline.set_startup_hook()


elif c__input_implementation:
    def c__input(prompt, prefill=''):
        raise CubissException("This function is not available due to missing implementation: {}"
                              .format(c__input_implementation))
else:
    def c__input(prompt, prefill=''):
        raise CubissException("This function is not available due to missing module. \n"
                              "Make sure you have 'readline' module (linux) or 'pyreadline' module (windows).")


def yes_no_input(prompt):
    while True:
        response = input(prompt)
        if response in ['Yes, Y, y, yes']:
            return True
        elif response in ['No, N, no, n']:
            return False
        else:
            continue


if __name__ == '__main__':
    print('This is just a library. Not a runnable script.')
