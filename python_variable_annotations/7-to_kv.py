def to_kv (k: str, v: int | float) -> tuple[str, float]:
    """Returns a tuple of k and the square of v."""
    return tuple(k, float(v))
