#!/usr/bin/python3
"""
a function that prints a square
Raises:
TypeError:
ValueError:
"""


def print_square(size):
    """
    a function to print a square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    print("{}\n".format("#" * size) * size, end="")
