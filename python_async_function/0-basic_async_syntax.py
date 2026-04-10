#!/usr/bin/env python3

import random
import asyncio
"""This module contains an asynchronous function that waits for a random delay
between 0 and a specified maximum delay."""


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay (inclusive) seconds
    and return the delay."""
    rand_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
