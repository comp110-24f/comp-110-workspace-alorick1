"""practice writing unit tests"""

__author__: str = "730668125"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_EV() -> None:
    """Should return the max of the list returns the expected value"""
    example: list[int] = [10, 9, 8, 7, 2]
    assert (find_and_remove_max(example)) == 10


def test_find_and_remove_max_mutates() -> None:
    """Should remove the max of the list and mutates the input in the expected way."""
    example: list[int] = [10, 9, 8, 7, 2]
    find_and_remove_max(example)
    assert example == [9, 8, 7, 2]


def test_find_and_remove_max_unconventional() -> None:
    """returns the correct value in case of an unconventional input."""
    assert find_and_remove_max([]) == -1
