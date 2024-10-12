#!/usr/bin/env python3
"""
duck type iterable object
annotating  function param and returning values
with appropriate types
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    annotating function parameters
    element_length
    """
    return [(i, len(i)) for i in lst]
