from c__lib.c__lib import CubissException
import re


def base_n(number, base, fill=(0, ''), symbols="0123456789abcdefghijklmnopqrstuvwxyz"):
    """Converts 'number' to string representation in specified base."""
    if base > len(symbols):
        raise CubissException(f'Not enough symbols for base {base}. Got f{len(symbols)}.')

    retval = \
        ((number == 0) and symbols[0]) \
        or \
        (base_n(number // base, base, symbols).lstrip(symbols[0]) + symbols[number % base])

    return fill[1] * (int(fill[0]) - len(retval)) + retval


def strip_split_text(text,
                     viable_chars=r'a-zA-Z0-9.,!?:'):
    """
    Strips text of any characters not included in viable_chars.
    Returns tuple (left removed, remaining, right removed).
    """

    match = re.match(
        f'(.*?)([{viable_chars}].*[{viable_chars}])(.*)',
        text)

    return match.group(1), match.group(2), match.group(3)


def size_to_string(size):
    """
    Format number of bytes with SI prefix. (i.e. '10 GB')
    :param size: Number of Bytes.
    :return: String representation of bytes.
    """
    if size < 9.999e3:
        return "{0:.1f} B".format(size)
    elif size < 9.999e6:
        return "{0:.1f} kB".format(size / 10e3)
    elif size < 9.999e9:
        return "{0:.1f} MB".format(size / 10e6)
    elif size < 9.999e12:
        return "{0:.1f} GB".format(size / 10e9)
    elif size < 9.999e15:
        return "{0:.1f} TB".format(size / 10e12)
    elif size < 9.999e18:
        return "{0:.1f} EB".format(size / 10e15)
    elif size < 9.999e21:
        return "{0:.1f} ZB".format(size / 10e18)
    elif size < 9.999e24:
        return "{0:.1f} YB".format(size / 10e21)


size_to_string.max_len = 8  # Maximal length of string returned by size_to_string.


def print_progress(progress, finish,
                   start_symbol='\r',
                   end_symbol='',
                   display_file_size=True,
                   progress_bar=True, progress_symbol='*', full_symbol='_', progress_bar_len=50):
    """
    Prints nicely formatted progress indicator.
    :param progress: How much is done.
    :param finish: How much is 100%.
    :param start_symbol: String that will be before progress bar.
    :param end_symbol: String that will be after progress bar.
    :param display_file_size: Whether text representation should be displayed. i.e. '[14/50]'
    :param progress_bar: Whether progress bar should be displayed. i.e. '(******_________)'
    :param progress_symbol: String representing one bit of finished progress. i.e. '*'
    :param full_symbol: String representing one bit of unfinished task. Should be same width as progress_symbol i.e. '_'
    :param progress_bar_len: Length of progress bar. i.e. 50
    :return: None
    """
    symbols = progress // (finish // progress_bar_len)

    if display_file_size and progress_bar:
        print(start_symbol +
              "{}/{} ".format(str(progress).rjust(len(str(progress)), ' '), str(finish)) +
              '[' +
              "".rjust(symbols, progress_symbol) +
              "".rjust(progress_bar_len - symbols, full_symbol) +
              ']',
              end=end_symbol)
    elif display_file_size:
        print(start_symbol +
              "{}/{}".format(str(progress).rjust(len(str(progress)), ' '), str(finish)),
              end=end_symbol)
    elif progress_bar:
        print(start_symbol +
              '[' +
              "".rjust(symbols, progress_symbol) +
              "".rjust(progress_bar_len - symbols, full_symbol) +
              ']',
              end=end_symbol)


def print_data_transfer_progress(progress, finish,
                                 start_symbol='\r',
                                 end_symbol='',
                                 display_file_size=True,
                                 progress_bar=True, progress_symbol='*', full_symbol='_', progress_bar_len=50):
    """
    Prints nicely formatted progress with file size indicator.
    :param progress: How much is done (in bytes).
    :param finish: How much is 100% (in bytes).
    :param start_symbol: String that will be before progress bar.
    :param end_symbol: String that will be after progress bar.
    :param display_file_size: Whether text representation should be displayed. i.e. '[14/50]'
    :param progress_bar: Whether progress bar should be displayed. i.e. '(******_________)'
    :param progress_symbol: String representing one bit of finished progress. i.e. '*'
    :param full_symbol: String representing one bit of unfinished task. Should be same width as progress_symbol i.e. '_'
    :param progress_bar_len: Length of progress bar. i.e. 50
    :return: None
    """
    symbols = progress // (finish // progress_bar_len)

    if display_file_size and progress_bar:
        print(start_symbol +
              "{}/{} ".format(size_to_string(progress).rjust(size_to_string.max_len, ' '), size_to_string(finish)) +
              '[' +
              "".rjust(symbols, progress_symbol) +
              "".rjust(progress_bar_len - symbols, full_symbol) +
              ']',
              end=end_symbol)
    elif display_file_size:
        print(start_symbol +
              "{}/{}".format(size_to_string(progress).rjust(size_to_string.max_len, ' '), size_to_string(finish)),
              end=end_symbol)
    elif progress_bar:
        print(start_symbol +
              '[' +
              "".rjust(symbols, progress_symbol) +
              "".rjust(progress_bar_len - symbols, full_symbol) +
              ']',
              end=end_symbol)


def seconds_to_czech_string(seconds):
    """Converts seconds to days/hours/minutes/seconds in czech language"""

    seconds = abs(int(seconds))

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    days_str = None
    hours_str = None
    minutes_str = None
    seconds_str = None

    if days > 0:
        days_str = f'{days}'
        if days == 1:
            days_str += f' den'
        elif days < 5:
            days_str += f' dny'
        else:
            days_str += f' dní'

    if hours > 0:
        hours_str = f'{hours}'
        if hours == 1:
            hours_str += ' hodina'
        elif hours < 5:
            hours_str += ' hodiny'
        else:
            hours_str += ' hodin'

    if minutes > 0:
        minutes_str = f'{minutes}'
        if minutes == 1:
            minutes_str += ' minuta'
        elif minutes < 5:
            minutes_str += ' minuty'
        else:
            minutes_str += ' minut'

    if seconds > 0:
        seconds_str = f'{seconds}'
        if seconds == 1:
            seconds_str += ' sekunda'
        elif seconds < 5:
            seconds_str += ' sekundy'
        else:
            seconds_str += ' sekund'

    ret = None

    parts = 0

    for t in (seconds_str, minutes_str, hours_str, days_str):
        if t is None:
            continue

        parts += 1

        if parts == 1:
            ret = f'{t}'
        elif parts == 2:
            ret = f'{t} a {ret}'
        else:
            ret = f'{t}, {ret}'

    return ret


if __name__ == '__main__':
    print('This is just a library. Not a runnable script.')
