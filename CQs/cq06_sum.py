"""Summing the elements of a list using different loops"""

__author__: str = "730668125"


def w_sum(vals: list[float]) -> float:
    """Calculates the sum of all the elemnts in the list using a while loop"""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum = sum + vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Calculates the sum of elements in a list using a for ... in ... loop."""
    sum: float = 0.0
    for elem in vals:
        sum = sum + elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculates the sum of elements in a list using a for ... in range(...) loop"""
    sum: float = 0.0
    for index in range(0, len(vals)):
        sum = sum + vals[index]
    return sum
