from __future__ import annotations

__author__ = "730668125"


class Node:
    # Class of a Node

    def __init__(self, value: int, next: Node | None):
        """Magic method to initialize each instance of Node"""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represent a Node object as a string"""
        rest: str = "?"  # initializes the value rest as "?"
        if self.next is None:
            rest = "None"  # When the node is the last one rest is set to "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of the node at the index called"""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        # Raises an error if the list is empty
        return head.value
    else:
        new_index: int = index - 1
        rest: int = value_at(head.next, new_index)
        return rest


def max(head: Node | None) -> int:
    """Returns the maximum value of the linked list"""
    if head is None:
        raise ValueError("Cannot call max with None")
    # Raises an error if the list is empty
    if head.next is None:
        return head.value
    else:
        rest: int = max(head.next)
        if head.value > rest:
            return head.value
        else:
            return rest


def linkify(items: list[int]) -> Node | None:
    if not items:
        return None
    else:
        rest: Node | None = linkify(items[1:])
        result: Node = Node(items[0], rest)
        return result


def scale(head: Node | None, factor: int) -> Node | None:
    if head is None:
        return None
    else:
        scaled_val: int = head.value * factor
        rest: Node | None = scale(head.next, factor)
        result: Node = Node(scaled_val, rest)
        return result
