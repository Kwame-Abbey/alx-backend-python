#!/usr/bin/env python3
"""Alter coroutine wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all delays"""
    delays = [task_wait_random(max_delay) for i in range(n)]
    delays = asyncio.as_completed(delays)
    all_delays = [await delay for delay in delays]
    return all_delays
