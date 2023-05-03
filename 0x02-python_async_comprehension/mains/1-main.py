#!/usr/bin/env python3
"""module docs for mains/1-main.py"""
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())
