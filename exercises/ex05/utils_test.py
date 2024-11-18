"""defining unit tests"""

__author__: str = "730668125"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_rv() -> None:
    """Test that only_evens returns the even values from a list."""
    example: list[int] = [2, 9, 15, 32, 77, 100]
    assert only_evens(example) == [2, 32, 100]


def test_only_evens_mutate() -> None:
    """Test that only_evens does not mutate the original list."""
    example: list[int] = [2, 9, 15, 32, 77, 100]
    original_example = example.copy()
    only_evens(example)
    assert example == original_example


def test_only_evens_edge() -> None:
    """Test that only_evens returns [] when the input list is empty."""
    assert only_evens([]) == []


def test_sub_rv() -> None:
    """Test that sub returns the correct subset of the list."""
    example: list[int] = [1, 2, 3, 4, 5]
    assert sub(example, 1, 4) == [2, 3, 4]


def test_sub_mutate() -> None:
    """Test that sub does not mutate the original list."""
    original_example: list[int] = [1, 2, 3, 4, 5]
    copy_example = original_example.copy()
    sub(original_example, 1, 4)
    assert original_example == copy_example


def test_sub_edge() -> None:
    """Test that sub returns [] for invalid slice parameters."""
    assert sub([], 0, 1) == []
    assert sub([1, 2, 3], 4, 5) == []
    assert sub([1, 2, 3], -1, 2) == []


def test_add_at_index_rv() -> None:
    """Test that add_at_index returns None."""
    example: list[int] = [1, 2, 3]
    assert add_at_index(example, 4, 1) is None


def test_add_at_index_mutate() -> None:
    """Test that add_at_index modifies the list correctly."""
    example: list[int] = [1, 2, 3]
    add_at_index(example, 0, 0)
    assert example == [1, 0, 2, 3]


def test_add_at_index_empty_list() -> None:
    """Test that add_at_index works on an empty list."""
    example = []
    add_at_index(example, 1, 0)
    assert example == [1]


def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for invalid indices."""
    example = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(example, 4, 4)
    with pytest.raises(IndexError):
        add_at_index(example, -1, 4)
