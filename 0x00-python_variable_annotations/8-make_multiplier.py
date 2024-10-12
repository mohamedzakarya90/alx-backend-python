#!/usr/bin/env python3
"""
complex types : functions
writting typed-annotated function make_multiplier
takes float multiplier argument
returning function which multiplies float by multipier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Typed-annotated function
    make_multiplier
    """

    def fn(num: float):
        return num * multiplier
    return fn
