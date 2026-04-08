#!/usr/bin/env python3
import typing
"""Defines a sum_mixed_list type-annotated function."""


def sum_mixed_list(mxd_list: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of all the elements of a list."""
    return sum(mxd_list)
