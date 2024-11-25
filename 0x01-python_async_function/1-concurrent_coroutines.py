#!/usr/bin/env python3
"""A module that executes multiple
coroutines at the same time with async"""


import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """executing multiple coroutines at the same time with async"""
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    results = await asyncio.gather(*tasks)
    for result in results:
        delays.append(result)

    sorted_delays = []
    while delays:
        smallest = min(delays)
        sorted_delays.append(smallest)
        delays.remove(smallest)

    return sorted_delays
