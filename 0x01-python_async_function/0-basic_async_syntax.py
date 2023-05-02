#!/usr/bin/env python3
"""Module Docs for 0-basic_async_syntax.py"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    The wait_random function will wait a random amount of time between 0 and
    max_delay seconds.

    max_delay: int: Specify the maximum delay in seconds
    return: A random number between 0 and max_delay
    """
    result = random.uniform(0, max_delay)
    await asyncio.sleep(result)
    return result
