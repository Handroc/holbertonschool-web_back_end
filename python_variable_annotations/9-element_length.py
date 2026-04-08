#!/usr/bin/env python3
from typing import Iterable, List, Sequence, Tuple
"""Defines an element_length type-annotated function."""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with the length of each element in lst."""
    return [(i, len(i)) for i in lst]
