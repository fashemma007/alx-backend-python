#!/usr/bin/python3
"""type-annotated function sum_list"""


def sum_list(input_list: list[float]) -> float:
    """
    The sum_list function takes a list of float point numbers and returns the
    sum of all the numbers.

    input_list: `list[float]`: Specifies the type of data that is being
    passed into the function
    return: A sum of all element in input_list
    """

    value: float = 0.0
    for num in input_list:
        value += num
    return value
