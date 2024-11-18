"""File to define Bear class."""

__author__ = "730668125"


class Bear:
    """A class to represent a Bear in the river ecosystem."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a Bear with age and hunger_score of 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Make a simulation of day passing for the Bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish) -> None:
        """Increase Bear's hunger_score by the  number of fish it eats."""
        self.hunger_score += num_fish
