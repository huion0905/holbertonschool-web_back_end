#!/usr/bin/env python3

"""
Script that defines 'sum_mixed_list' function
which takes a list of integers or floats
and returns the sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of a list containing both integers and floats"""
    return sum(mxd_lst)
