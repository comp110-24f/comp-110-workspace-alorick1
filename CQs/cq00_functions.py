"""cq00_functions"""

__author__ = "730668125"


def mimic(message: str) -> str:
    """it is repeating the word back to me"""
    return message


def main() -> None:
    """it is combining two functions"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
