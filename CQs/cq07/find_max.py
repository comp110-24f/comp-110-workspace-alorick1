"""practice writing a function that modifies a list """

__author__: str = "730668125"


def find_and_remove_max(number: list[int]) -> int:
    """Finds the max in the list and removes it"""
    if len(number) == 0:
        return -1
    else:
        idx: int = 0
        max_v: int = number[0]

        while idx < len(number):
            """continue this until the number is the max"""
            if number[idx] > max_v:
                max_v = number[idx]
            idx += 1

        idx_0: int = 0
        """Removes the max once it is found"""
        while idx_0 < len(number):
            if number[idx_0] == max_v:
                number.pop(idx_0)
            else:
                idx_0 += 1
        return max_v
