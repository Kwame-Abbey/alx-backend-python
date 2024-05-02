#!/usr/bin/env python3
"""Defines a type annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of list of floats"""
    return sum(input_list)
