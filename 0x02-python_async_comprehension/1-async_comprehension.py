#!/usr/bin/env python3
"""A module that writes Async Comprehensions"""


import asyncio
import random
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """coroutine that collect 10 random numbers using an async
    comprehensing over async_generator
    then return the 10 random numbers."""

    result = [item async for item in async_generator()]
    return result