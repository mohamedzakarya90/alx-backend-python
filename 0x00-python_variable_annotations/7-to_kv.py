#!/usr/bin/env python3
"""
complex types : string and int-float to tuple
writting typed-annotated function to_kv which takes str k and int OR float v
returning  tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    typed-annotated function
    to_kv
    """
    return (k, v * v)
