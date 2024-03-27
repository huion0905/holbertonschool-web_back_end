#!/usr/bin/env python3

"""Creates a async coroutine that use the 0-basic_async_syntax module"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio.Task for the wait_random coroutine
    with the given max_delay."""
    coroutine = wait_random(max_delay)

    task = asyncio.create_task(coroutine)

    return task
