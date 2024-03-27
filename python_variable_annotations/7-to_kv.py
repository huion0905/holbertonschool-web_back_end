#!/usr/bin/env python3

"""
Script that defines 'to_kv' function
which takes a string and int/float
and returns a a tuple.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with the string k and the square of the int/float v"""
    return k, float(v ** 2)
