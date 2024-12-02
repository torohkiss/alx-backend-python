#!/usr/bin/env python3
"""A module that writes an Async Generator"""


import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """A coroutine async_generator that takes no arguments"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
