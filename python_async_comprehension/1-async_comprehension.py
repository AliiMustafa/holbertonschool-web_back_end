#!/usr/bin/env python3
"""Module for collect random numbers"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension() -> List[float]:
    """Function for collect random numbers"""
    return [i async for i in async_generator()]