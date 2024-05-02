#!/usr/bin/env python3
"""Defines a type-annonated"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, v * v)
