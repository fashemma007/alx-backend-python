#!/usr/bin/env python3
"""module docs for 1-async_comprehension.py"""

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The async_comprehension function returns a list of floats.

    return: A list of floats
    """
    # list comprehension for async generators
    return [rez async for rez in async_generator()]
