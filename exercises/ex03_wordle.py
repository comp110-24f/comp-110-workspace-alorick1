"""creating wordle using emojis and f strings"""

__author__ = "730668125"


def input_guess(secret_word_len: int) -> str:
    """Asks the user for a guess of the secret word."""
    while True:
        guess = input(f"Enter a {secret_word_len} character word: ")
        if len(guess) == secret_word_len:
            return guess
        else:
            print(f"That wasn't {secret_word_len} chars! Try again:")


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if a character is present in the secret word."""
    assert len(char_guess) == 1, "char_guess must be a single character"
    for char in secret_word:
        if char == char_guess:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Generates an emoji representation of the guess compared to the secret word."""
    assert len(guess) == len(secret), "Guess and secret must have the same length"
    emoji = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    return emoji


WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"


def main(secret: str) -> None:
    """The main game loop of the Wordle game."""

    maximum_turns = 6
    number_of_turns_used = 0
    winner = False

    while number_of_turns_used < maximum_turns and not winner:
        number_of_turns_used += 1
        print(f"=== Turn {number_of_turns_used}/{maximum_turns} ===")
        guess = input_guess(len(secret))
        emoji_result = emojified(guess, secret)
        print(emoji_result)

        if guess == secret:
            winner = True

    if winner:
        print(f"You won in {number_of_turns_used}/{maximum_turns} turns!")
    else:
        print(f"X/{maximum_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
