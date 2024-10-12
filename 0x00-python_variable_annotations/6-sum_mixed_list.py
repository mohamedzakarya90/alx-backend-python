#!/usr/bin/env python3
"""
complex types : mixed list
Writting  typed-annotated function sum_mixed_list
which takes mxd_lst integers and floats
returning their sum as float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    typed-annotated function
    sum_mixed_list
    """
    return sum(mxd_lst)
