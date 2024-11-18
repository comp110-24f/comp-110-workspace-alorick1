"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730668125"


def input_word() -> str:
    """Prompts the user for a 5-character word and returns it to them."""
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # Exit the program if the word is too long or short
    return word  # Returns the 5 letter word


def input_letter() -> str:
    """Prompts the user for a single character and returns it to them."""
    letter = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # Exit the program if the letter is too long
    return letter  # Returns the letter


def contains_char(word: str, letter: str) -> None:
    """Checks if the letter is in the word and prints the results of if/how many times the letter is in the word."""
    print("Searching for " + letter + " in " + word)

    index = 0  # Initialize the index
    number_of_letters = 0  # Initialize the count to 0

    while index < len(word):
        if word[index] == letter:
            number_of_letters += 1
            print(letter + " found at index " + str(index))
        index += 1  # Increment the index

    if number_of_letters == 0:
        print("No instances of " + letter + " found in " + word)
    elif number_of_letters == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(number_of_letters) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Main function that runs the program."""
    word = input_word()  # 5 letter word
    letter = input_letter()  # 1 letter
    contains_char(word, letter)  # Check for if the letter is in the word


if __name__ == "__main__":
    main()
