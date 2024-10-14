#!/usr/bin/env python3
'''Asyncronous Python
'''
from typing import List
import asyncio


time_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''return a list of awaited response from previous function'''
    lis = []
    for i in range(n):
        ma = await wait_random(max_delay)
        lis.append(ma)
    return sorted(lis)
