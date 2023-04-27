#!/usr/bin/python3
"""type-annotated function sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    The sum_mixed_list function takes a list of mixed integers and floats
    as an argument, and returns the sum of all numbers in the list.

    mxd_lst: List[Union[int, float]]: the list that is being passed in
    return: The sum of the elements in a list
    """
    value: float = 0
    for num in mxd_lst:
        value += num
    return value
