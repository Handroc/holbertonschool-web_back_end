#!/usr/bin/env python3
import typing
"""Defines a sum_list type-annotated function."""


def sum_list(input_list: typing.List[float]) -> float:
    """Returns the sum of all the elements of a list."""
    return sum(input_list)
