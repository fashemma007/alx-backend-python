#!/usr/bin/env python3
"""module docs for 3-tasks.py"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Method: Returns a asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
