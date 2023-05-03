#!/usr/bin/env python3
"""module docs for 2-measure_runtime.py"""

import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel using
    asyncio.gather
    """
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = perf_counter()
    runtime = end_time - start_time
    return runtime
