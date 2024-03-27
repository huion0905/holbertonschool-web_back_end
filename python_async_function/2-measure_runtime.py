#!/usr/bin/env python3

"""Creates a async coroutine that use the wait_n function
from '1-concurrent_coroutines' module"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n."""
    # Takes the start time
    start_time = time.time()

    # Run the wait_n async coroutine
    asyncio.run(wait_n(n, max_delay))

    # Takes the end time
    end_time = time.time()

    # Calculate the total time of execution of the coroutine
    total_time = end_time - start_time

    # Returns the average execution time per iteration
    return total_time / n
