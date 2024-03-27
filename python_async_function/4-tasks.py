#!/usr/bin/env python3

"""Creates a async coroutine that use the 3-tasks module"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that spawns wait_random n times
    with the specified max_delay."""
    delays = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    delays.extend(results)

    return sorted(delays)
