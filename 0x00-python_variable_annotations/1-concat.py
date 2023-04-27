#!/usr/bin/python3
"""type-annotated function that returns a concatenated string of 2 args"""


def concat(a: str, b: str) -> str:
    """
    The concat function takes two strings and returns a new string
    that is the concatenation of the two input strings.

    a: str
    b: str
    return: A string that is the concatenation of a and b
    """
    return a + b
