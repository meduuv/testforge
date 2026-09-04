"""Test data generation helpers."""

def cases(values: list[object]) -> list[tuple[int, object]]:
    """Attach stable numeric case IDs to values."""
    return list(enumerate(values, 1))
