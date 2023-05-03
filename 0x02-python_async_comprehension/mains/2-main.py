#!/usr/bin/env python3
"""module docs for mains/2-main.py"""
import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
