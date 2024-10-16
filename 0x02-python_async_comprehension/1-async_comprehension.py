#!/usr/bin/env python3
"""generatting list fom async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collecting async generated list and returning it"""
    return [_ async for _ in async_generator()]
