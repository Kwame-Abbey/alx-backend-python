#!/usr/bin/env python3
"""Executes multiple coroutines at the same time"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all delays"""
    delays = [wait_random(max_delay) for i in range(n)]
    delays = asyncio.as_completed(delays)
    all_delays = [await delay for delay in delays]
    return all_delays
