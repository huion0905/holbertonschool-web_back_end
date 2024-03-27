#!/usr/bin/env python3

"""Module that computes index range for the pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple (start_index, end_index)
    for a given page and page size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
