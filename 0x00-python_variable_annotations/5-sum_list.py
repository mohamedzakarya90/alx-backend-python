#!/usr/bin/env python3
"""
complex types : list of floats
writing type-annotated function sum_list which takes input_list of floats
as arguments
returning their sum as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    typed-annotated function
    sum_list
    """
    return sum(input_list)
