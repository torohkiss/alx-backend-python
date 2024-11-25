#!/usr/bin/env python3
"""A module that returns a asyncio.Task
from a synchronous function"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """Returns asyncio.Task from a sync function"""

    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
