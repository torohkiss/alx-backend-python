#!/usr/bin/env python3
"""A module about The basics of async"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """an asynchronous coroutine that takes in an integer
    argument (max_delay, with a default value of 10) named
    wait_random that waits for a random delay between 0
    and max_delay (included and float value)
    seconds and eventually returns it.
    """

    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
