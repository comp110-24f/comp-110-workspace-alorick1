"""List Utility Functions"""

__author__: str = "730668125"


def all(data: list[int], int_par: int) -> bool:
    """Checks if all elements in the list are the same as the given value."""
    index = 0
    if len(data) == 0:
        return False
    while index < len(data):
        if data[index] != int_par:
            return False
        index += 1
    return True


def max(data: list[int]) -> int:
    """Finds the maximum value in the list."""
    if len(data) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        biggest_num = data[0]
        index: int = 0
    while index < len(data):
        if data[index] > biggest_num:
            biggest_num = data[index]
        index += 1
    return biggest_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists are equal"""
    if len(list1) != len(list2):
        return False
    else:
        index = 0
        while index < len(list1):
            if list1[index] != list2[index]:
                return False
            index += 1
        return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Appends the elements of the second list to the first list."""
    index = 0
    while index < len(list2):
        list1.append(list2[index])
        index += 1
