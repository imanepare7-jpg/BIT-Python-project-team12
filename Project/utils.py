import os

def clear_screen():
    """Clears the terminal depending on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Pauses and waits for the user to press Enter."""
    input("\n  [Press Enter to continue...]")


def display_header(school_name):
   
    print("\n" + "="*55)
    print(f"   {school_name}")
    print(f"   School Management System v1.0")
    print("="*55)


def read_float(message, minimum = 0, maximum = 20) -> float:
    """
    Reads a valid decimal number between minimum and maximum.
    Uses a while loop and handles errors with try/except.
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


def read_integer(message, minimum = 1) -> int:
    """
    Reads a valid integer >= minimum.
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
