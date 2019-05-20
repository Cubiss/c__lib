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

    return  match.group(1), match.group(2), match.group(3)

if __name__ == '__main__':
    print('This is just a library. Not a runnable script.')
