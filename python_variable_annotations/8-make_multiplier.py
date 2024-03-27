#!/usr/bin/env python3

"""
Script that defines 'make_multiplier' function
which takes a float as argument
and returns a function that multiplies
a float by multiplier.
"""

from typing import Callable, Union


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create and return a function that multiplies
    a float by the given multiplier"""
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
