#!/usr/bin/env python3

"""
Script that defines 'sum_list' function which takes a list of floats
and returns the sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of floats"""
    result = 0
    for num in input_list:
        result += num

    return float(result)
