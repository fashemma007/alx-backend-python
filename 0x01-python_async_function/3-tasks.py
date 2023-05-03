#!/usr/bin/env python3
"""module docs for 3-tasks.py"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    The task_wait_random function creates a task that waits for a random delay
    between 0 and max_delay seconds. The function returns the created task.

    max_delay: int: Specify the maximum delay in seconds
    return: A task
    """
    async_task = asyncio.create_task(wait_random(max_delay))
    return async_task
