#!/usr/bin/env python3
"""Defines a type annotated function"""


def sum_list(input_list: list[float]) -> float:
    """Returns the sum of list of floats"""
    return sum(input_list)
