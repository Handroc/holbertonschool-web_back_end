#!/usr/bin/env python3
"""Defines a to_kv type-annotated function."""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """Returns a tuple of k and the square of v."""
    return (k, float(v))
