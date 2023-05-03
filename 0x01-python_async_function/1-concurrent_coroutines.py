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
    # call the wait_random functn n times
    awaited_result = [wait_random(max_delay) for _ in range(n)]
    # print(f"Your long awaited_result\n{awaited_result}")
    # use as_completed to return completed funcs as they complete
    awaited_result = asyncio.as_completed(awaited_result)
    # get the results from each promise/future
    result = [await future for future in awaited_result]
    return result
