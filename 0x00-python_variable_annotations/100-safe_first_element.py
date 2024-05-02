#!/usr/bin/env python3
"""Defines a type annotation function"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element or None"""
    if lst:
        return lst[0]
    else:
        return None
