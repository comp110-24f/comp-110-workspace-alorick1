"""implement some more list utility functions,"""

__author__: str = "730668125"


def only_evens(numbers: list[int]) -> list[int]:
    """Returns a new list containing only elements of the list that are even."""
    list_evens: list[int] = []
    idx: int = 0
    while idx < len(numbers):
        if numbers[idx] % 2 == 0:
            list_evens.append(numbers[idx])
        idx += 1
    return list_evens


def sub(numbers: list[int], beginning_idx: int, end_idx: int) -> list[int]:
    """Generates a subset of all the inputs."""
    if len(numbers) == 0:
        return []
    if beginning_idx >= len(numbers):
        return []
    if end_idx <= 0:
        return []
    if end_idx > len(numbers):
        end_idx = len(numbers)
    if beginning_idx < 0:
        beginning_idx = 0
    subset: list[int] = []
    idx: int = beginning_idx

    while idx < end_idx:
        subset.append(numbers[idx])
        idx += 1
    return subset


def add_at_index(input: list[int], first_int: int, idx: int) -> None:
    """Adds first_int to the list at the specified index."""
    if idx < 0 or idx > len(input):
        raise IndexError("Index is out of bounds for the input list")

    input.append(0)

    for idx_1 in range(len(input) - 1, idx, -1):
        input[idx_1] = input[idx_1 - 1]

    input[idx] = first_int
    return None
