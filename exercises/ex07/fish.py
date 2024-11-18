"""File to define Fish class."""

_author__ = "730668125"


class Fish:
    """A class to represent a Fish in the river ecosystem."""

    age: int

    def __init__(self):
        """Initialize a Fish with the age of 0."""
        self.age = 0

    def one_day(self) -> None:
        """Runs a simulation of one day passing for the Fish."""
        self.age += 1
