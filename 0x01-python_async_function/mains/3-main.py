#!/usr/bin/env python3
"""module docs for mains/3-main.py"""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
