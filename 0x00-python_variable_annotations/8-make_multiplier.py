#!/usr/bin/python3
"""type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """`make_multiplier` that takes a float `multiplier` as argument and
    returns a function that multiplies a float by `multiplier`
    """
    def multiply(args: float) -> float:
        """nested multiplier"""
        return multiplier * args
    return multiply
