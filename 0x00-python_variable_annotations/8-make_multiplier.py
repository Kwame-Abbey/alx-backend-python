#!/usr/bin/env python3
"""Defines a type-annonated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns that multiplies a float by multiplier"""
    return lambda x: x * multiplier
