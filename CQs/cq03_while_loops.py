"""practice using a while loop"""

__author__: str = "730668125"


def num_instances(phrase: str, search_char: str) -> int:
    # defines the count of occurrences
    index: int = 0
    # giving the index an initial value of 0
    count: int = 0
    # giving the count an initial value of 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count += 1
        index += 1
        # increases the count and index everytime you use search_char

    return count
