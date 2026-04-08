#!/usr/bin/env python3
import typing
"""Defines a to_kv type-annotated function."""


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Returns a tuple of k and the square of v."""
    return (k, float(v))
