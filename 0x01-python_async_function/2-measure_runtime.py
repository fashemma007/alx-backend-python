#!/usr/bin/env python3
"""module docs for 2-measure_runtime.py"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    The measure_time function measures the time it takes to execute wait_n
        coroutines concurrently.

    n: int: Specify the number of times to wait
    max_delay: int: Set the maximum delay for each task
    return: The average time of a single await call
    """
    start = time.perf_counter()  # start time
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()  # end time
    runtime = end - start  # function runtime
    return runtime / n
