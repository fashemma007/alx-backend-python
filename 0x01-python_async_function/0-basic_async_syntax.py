#!/usr/bin/env python3
"""Module Docs for 0-basic_async_syntax.py"""

import random


async def wait_random(max_delay: int = 10):
    """
    The wait_random function will wait a random amount of time between 0 and
    max_delay seconds.

    max_delay: int: Specify the maximum delay in seconds
    return: A random number between 0 and max_delay
    """
    result = random.randint(0, max_delay) + random.random()
    # make sure the returning value doesn't exceed limit
    while result > max_delay:
        result = random.randint(0, max_delay) + random.random()
    return result
