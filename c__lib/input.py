# version 1.0.0
from c__lib.misc import get_platform, CubissException

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
        Readline = None
        c__input_implementation = False

# c__input
if c__input_implementation == 'linux':
    def c__input(prompt, prefill: str = ''):
        readline.set_startup_hook(lambda: readline.insert_text(prefill))
        try:
            return input(prompt)
        finally:
            readline.set_startup_hook()
elif c__input_implementation == 'windows':
    def c__input(prompt, prefill: str = '', log_function=None):
        try:
            if prefill != '' and prefill is not None:
                if log_function is not None:
                    log_function(f'Prefill is not supported: {prefill}')
            return input(prompt)
        finally:
            readline.set_startup_hook()


elif c__input_implementation:
    def c__input(prompt: str, prefill='', log_function=None):
        if prefill != '' and prefill is not None:
            if log_function is not None:
                log_function(f'Prefill is not supported: {prefill}')
        if prompt != '' and prompt is not None:
            if log_function is not None:
                log_function(f'Prompt is not supported: {prefill}')
        raise CubissException("This function is not available due to missing implementation: {}"
                              .format(c__input_implementation))
else:
    def c__input(prompt: str, prefill='', log_function=None):
        if prefill != '' and prefill is not None:
            if log_function is not None:
                log_function(f'Prefill is not supported: {prefill}')
        if prompt != '' and prompt is not None:
            if log_function is not None:
                log_function(f'Prompt is not supported: {prefill}')
        raise CubissException("This function is not available due to a missing module. \n"
                              "Make sure you have 'readline' module (linux) or 'pyreadline' module (windows).")


def yes_no_input(prompt: str, yes_responses: list = None, no_responses: list = None, ignore_case=True):
    """
    Displays prompt and waits for 'right' answer (yes/no and abbreviations])
    :param prompt: Message to be displayed until user gives correct answer.
    :param yes_responses: Answers which return true. [y, yes] by default.
    :param no_responses: Answers which return false. [n, no] by default.
    :param ignore_case: Ignore case when matching answer with possible responses.
    :return: True if user's answer is in yes_responses.
    """

    yes_responses = yes_responses or ['y', 'yes', 'Y', 'Yes']
    no_responses = no_responses or ['no', 'n', 'N', 'No']

    while True:
        response = input(prompt)
        if (response.lower() if ignore_case else response) in \
                [r.lower() if ignore_case else r for r in yes_responses]:
            return True
        elif (response.lower() if ignore_case else response) in \
                [r.lower() if ignore_case else r for r in no_responses]:
            return False
        else:
            continue


def multiple_choice_input(prompt: str, choices, ignore_case=True):
    """
    Displays multiple choice prompt and waits for 'right' answer (number/key in choices dict)
    :param prompt: Message to be displayed until user gives correct answer.
    :param choices: An iterable of choices.
                    If it is dictionary, choices will be displayed as '<key>) <value>' and chosen key will be returned.
                    If it is other iterable, choices will be displayed as '<index>) <value>' and index will be returned.
    :param ignore_case: Ignore case when matching answer with possible responses.
    :return: Key (or index) of chosen answer.
    """
    if len(choices) < 1:
        raise CubissException('There must be at least one choice.')

    if not issubclass(type(choices), dict):
        choices = {key: value for key, value in enumerate(choices)}

    choices = {str(key).lower() if ignore_case else str(key): value for key, value in choices.items()}

    while True:
        print(prompt)
        for key, value in choices.items():
            print(f'{str(key)}) {value}')
        response = input()

        if (response.lower() if ignore_case else response) in choices.keys():
            return choices[response]
        else:
            continue


if __name__ == '__main__':
    print('This is just a library. Not a runnable script.')
