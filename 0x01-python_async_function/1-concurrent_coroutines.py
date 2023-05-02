#!/usr/bin/env python3
"""module docs for 1-concurrent_coroutines.py"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    The wait_n function should wait for n seconds, and return a list of
    n random numbers.

    n: int: Specify the number of times to call wait_random
    max_delay: int: Set the maximum delay for each task
    return: A list of n floats
    """
    f_time = [wait_random(max_delay) for _ in range(n)]
    f_time = asyncio.as_completed(f_time)
    lag = [await future for future in f_time]
    return lag
