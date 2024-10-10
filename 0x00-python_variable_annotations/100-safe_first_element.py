#!/usr/bin/env python3
"""
duck typing : first element of  sequence
augument code with a correct duck-typed annotations
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    duck-typed function
    safe_first_element
    """
    if lst:
        return lst[0]
    else:
        return None
