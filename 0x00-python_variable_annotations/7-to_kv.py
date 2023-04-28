#!/usr/bin/env python3
"""type-annotated function to_kv"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of string, float"""
    return (k, v**2)
