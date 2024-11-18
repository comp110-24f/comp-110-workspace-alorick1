"""Practicing with coniditonals, local variables, and user input"""

__author__: str = "730668125"


def guess_a_number() -> None:
    """Guesses the number"""
    secret: int = 7
    word: int = int(input("Guess a number: "))
    """Giving the number a name"""
    print("Your guess was " + str(word))
    if word == secret:
        print("You got it!")
        """Perfect guess"""
    elif word < secret:
        print("Your guess was too low! The secret number is " + str(secret))
        """Too small of a number"""
    else:
        print("Your guess was too high! The secret number is " + str(secret))
        """Too big of a number"""
    return None


if __name__ == "__main__":
    guess_a_number()
"""Calls the function"""
