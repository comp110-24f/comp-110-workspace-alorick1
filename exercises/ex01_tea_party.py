"""planning a tea party for guests and buying the supplies"""

__author__: str = "730668125"


def main_planner(guests: int) -> None:
    """gives us tea bags, treats, and cost together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# putting all the parts together for a tea party, amount of guests, tea needed, treats, etc


def tea_bags(
    people: int,
) -> int:
    """ "tells us the amount of teabags needed"""
    return people * 2


# figuring out how many tea bags are needed based off the amount of people attending


def treats(
    people: int,
) -> int:
    """tells us the amount of treats needed"""
    return int((tea_bags(people=people)) * 1.5)


# figuring out how many treats are needed based off the amount of tea each person attending will drink


def cost(tea_count: int, treat_count: int) -> float:
    """tells us the cost of the teabags and treats"""
    return (tea_count * 0.5) + (treat_count * 0.75)


# finding the cost of the teabags and treats based off the amount of people attending


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
