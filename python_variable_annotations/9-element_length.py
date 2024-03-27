#!/usr/bin/env python3

"""
Script that defines 'element_length' function which
takes an Iterable of sequences and
returns a list of tuples with a sequence as first element
and an int for second element.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element in the input list"""
    return [(i, len(i)) for i in lst]
