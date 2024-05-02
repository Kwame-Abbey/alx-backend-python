#!/usr/bin/python3
"""Defines a duck Type"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a tuple"""
    return [(i, len(i)) for i in lst]
