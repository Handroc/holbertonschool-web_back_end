#!/usr/bin/env python3
"""
Spawns wait_random n times with a specified max_delay.
"""
import asyncio
from typing import List

# Importing wait_random from the previous file
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times.
    
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.
        
    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    # Create a list of tasks to be executed concurrently
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # asyncio.as_completed yields results as soon as they are ready
    # Since wait_random returns after a sleep, the shortest delays 
    # will finish first, effectively sorting them automatically.
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays
