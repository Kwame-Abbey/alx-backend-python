#!/usr/bin/env python3
"""Defines a type annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum"""
    return sum(mxd_lst)
