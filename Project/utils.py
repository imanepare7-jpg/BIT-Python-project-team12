"""
utils.py
--------
Utility functions reused across all menus.
Imported by menus.py and main.py
"""

import os


def clear_screen():
    """Clears the terminal depending on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    """Pauses and waits for the user to press Enter."""
    input("\n  [Press Enter to continue...]")


def display_header(school_name: str):
    """
    Displays the application header.
    :param school_name: school name to display
    """
    print("\n" + "="*55)
    print(f"   {school_name}")
    print(f"   School Management System v1.0")
    print("="*55)


def read_float(message: str, minimum: float = 0, maximum: float = 20) -> float:
    """
    Reads a valid decimal number between minimum and maximum.
    Uses a while loop and handles errors with try/except.
    :param message: message displayed to the user
    :param minimum: minimum accepted value
    :param maximum: maximum accepted value
    :return: valid float
    """
    while True:
        try:
            value = float(input(message))       # str -> float conversion
            if minimum <= value <= maximum:
                return value
            else:
                print(f"  [!] Please enter a value between {minimum} and {maximum}.")
        except ValueError:
            print("  [!] Please enter a valid number.")


def read_integer(message: str, minimum: int = 1) -> int:
    """
    Reads a valid integer >= minimum.
    :param message: message displayed to the user
    :param minimum: minimum accepted value
    :return: valid integer
    """
    while True:
        try:
            value = int(input(message))         # str -> int conversion
            if value >= minimum:
                return value
            else:
                print(f"  [!] Please enter a number >= {minimum}.")
        except ValueError:
            print("  [!] Please enter a valid integer.")