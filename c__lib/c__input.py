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
    def c__input(prompt, prefill=''):
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


def yes_no_input(prompt, yes_responses: list = None, no_responses: list = None):
    """
    Displays prompt and waits for 'right' answer (yes/no and abbreviations])
    :param prompt: Message to be displayed until user gives correct answer.
    :param yes_responses: Answers which return true. [y, yes] by default.
    :param no_responses: Answers which return false. [n, no] by default.
    :return: True if user's answer is in yes_responses.
    """

    yes_responses = yes_responses or ['y', 'yes']
    no_responses = no_responses or ['no', 'n']

    while True:
        response = input(prompt)
        if response.lower() in yes_responses:
            return True
        elif response.lower() in no_responses:
            return False
        else:
            continue


if __name__ == '__main__':
    print('This is just a library. Not a runnable script.')
