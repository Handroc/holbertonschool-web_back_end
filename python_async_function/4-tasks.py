#!/usr/bin/env python3
"""
Spawns task_wait_random n times with a specified max_delay.
"""
import asyncio
from typing import List

# Import wait_n from the previous implementation
# and task_wait_random as defined in your requirements
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times.
    
    Args:
        n (int): The number of times to spawn the task.
        max_delay (int): The maximum delay for each task.
        
    Returns:
        List[float]: List of delays in ascending order.
    """
    # Create a list of Tasks using the task_wait_random function
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Collect results as they finish to ensure ascending order
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays
