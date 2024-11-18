"""Practicing dictonary functions"""

__author__: str = "730668125"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary"""
    inverted_dict: dict[str, str] = {}
    for key, value in dictionary.items():
        if value in inverted_dict:
            raise KeyError("error duplicate key")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(favorites: dict[str, str]) -> str:
    """Figures out the most popular favorite color"""
    color_count: dict[str, int] = {}
    for color in favorites.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    max_color: str = ""
    max_count: int = -1

    for color, count in color_count.items():
        if count > max_count:
            max_color = color
            max_count = count
        elif count == max_count:
            favorite_values: list[str] = list(favorites.values())
            first_color_index: int = favorite_values.index(max_color)
            current_color_index: int = favorite_values.index(color)
            if current_color_index < first_color_index:
                max_color = color

    return max_color


def count(values: list[str]) -> dict[str, int]:
    """Will count the number of times that a value appears in the values list"""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorizes the words list into a dictionary"""
    result: dict[str, list[str]] = {}
    for word in words:
        first_letter: str = word[0].lower()
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(word)
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Will mutate the attendance"""
    if day not in attendance:
        attendance[day] = []
    if student not in attendance[day]:
        attendance[day].append(student)
