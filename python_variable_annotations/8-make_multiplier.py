#!/usr/bin/env python3
import typing
"""Defines a make_multiplier type-annotated function."""


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
