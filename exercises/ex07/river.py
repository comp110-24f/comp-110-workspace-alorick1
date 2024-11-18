"""File to define River class."""

__author__ = "730668125"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """A class to represent a River ecosystem with Bears and Fish."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """Initialize the River with a specified number of Fish and Bears."""
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]
        self.day = 0

    def view_river(self) -> None:
        """Display the current day, fish population, and bear population in theriver."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self) -> None:
        """Simulate one day passing for both the bears and fish in the river."""
        for fish in self.fish:
            fish.one_day()
        for bear in self.bears:
            bear.one_day()
        self.day += 1

    def one_river_week(self) -> None:
        """Simulate one week passing in the river."""
        for _ in range(7):
            self.one_river_day()

    def check_ages(self) -> None:
        """Remove the Fish that are older than 3 and the Bears that are older than 5."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int) -> None:
        """Remove a specified amount of Fish from the front of the list."""
        idx = 0
        while idx < amount:
            if self.fish:
                self.fish.pop(0)
            idx += 1

    def bears_eating(self) -> None:
        """Simulate Bears eating Fish if there are enough Fish available."""
        bear_count = 0
        while bear_count < len(self.bears) and len(self.fish) >= 5:
            self.remove_fish(3)
            self.bears[bear_count].eat(3)
            bear_count += 1

    def check_hunger(self) -> None:
        """Remove the Bears with hunger_score less than 0."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_bears(self) -> None:
        """Add new Bears to the river based on the current Bear population."""
        new_bears = len(self.bears) // 2
        while new_bears > 0:
            self.bears.append(Bear())
            new_bears -= 1

    def repopulate_fish(self) -> None:
        """Add new Fish to the river based on the current Fish population."""
        new_fish = (len(self.fish) // 2) * 4
        while new_fish > 0:
            self.fish.append(Fish())
            new_fish -= 1
