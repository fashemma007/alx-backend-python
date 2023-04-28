#!/usr/bin/env python3
"""Module Docs"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """alx didnt gimme docstrings either"""
    return [(i, len(i)) for i in lst]
