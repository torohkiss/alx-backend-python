#!/usr/bin/env python3
"""Checks Run time for four parallel comprehensions"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return"""

    start_time = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = time.time()
    return end_time - start_time
