"""Mutating functions."""

__author__: str = "730668125"


def manual_append(list: list[int], value: int) -> None:
    """appends numbers based on the value"""
    list.append(value)
    return None


def double(list: list[int]) -> None:
    """doubles all of the numbers in the list"""
    idx: int = 0
    while idx < len(list):
        list[idx] = list[idx] * 2
        idx += 1
    return None


list_1 = [1, 2, 3]
list_2 = list_1.copy()
# setting the two lists equal

double(list_2)
# doubling list 2

print(list_1)  # both lists are the same
print(list_2)  # same output as list_1
