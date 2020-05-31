'''Testing exceptions in python from PluralSight

Usage:
    python3 exception.py
'''

import sys
from math import log

DIGIT_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def convert(s):
    '''Convert a LIST where each element is the string representation of a single digit into its
    equivalent integer

    Args:
        s: list with digit name string - e.g. ["three", "five", "two", "zero"]

    Returns:
        equivalent integer to s - e.g. 3520 or raise exception for error
    '''

    try:
        number = ''
        for token in s:
            # print(f"token = {token}")
            number += DIGIT_map[token]
        return int(number)
        # print(f"Conversion success! x = {x}")
    except (KeyError, TypeError) as e:
        print(f"Conversion failure: {e!r}", file=sys.stderr)
        raise

def string_log(s):
    """Convert a LIST where each element is the string representation of a single digit into its
    equivalent integer and returns the log of such number

    Args:
        s: list with digit name string - e.g. ["three", "five", "two", "zero"]

    Returns:
        log of equivalent integer to s - e.g. log (3520) or raise exception for error
    """

    v = convert(s)
    return log(v)
