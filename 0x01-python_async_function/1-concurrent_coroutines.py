#!/usr/bin/env python3
'''Asyncronus python
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    lis = []
    for i in range(n):
        ma = await wait_random(max_delay)
        lis.append(ma)
    return sorted(lis)
