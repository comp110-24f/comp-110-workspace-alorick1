"""Basic syntax of lists."""

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

my_numbers.append(1.5)  # add a number to the list

game_points: list[int] = [102, 86, 94]  # Create an already populated list

last_game: int = game_points[2]
print(last_game)
print(game_points[2])  # Indexing the list

game_points[1] = 72  # Modifying elements (because list are mutable)
print(game_points)

print(len(game_points))  # Getting the length

game_points.pop(1)  # Remove an element
print(game_points)


# Write a function called display the input is a list of integers the return value is none loop over the input nad print every value and try calling it on game_prints
def display(Input: list[int]) -> None:
    index: int = 0
    while index < len(Input):
        print(Input[index])
        index += 1


display(Input=game_points)

