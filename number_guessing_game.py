"""
Number Guessing Game
---------------------
A simple console-based game that demonstrates:
- random number generation
- loops (while)
- conditional statements (if/elif/else)
- user input/output
- functions
"""

import random


def get_difficulty():
    """Ask the player to choose a difficulty level and return (range, max_attempts)."""
    print("\nChoose a difficulty level:")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return 1, 50, 10
        elif choice == "2":
            return 1, 100, 7
        elif choice == "3":
            return 1, 200, 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def get_guess(low, high):
    """Prompt the player for a valid integer guess within the given range."""
    while True:
        raw = input(f"Enter your guess ({low}-{high}): ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("That's not a valid number. Try again.")
            continue

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        return guess


def play_round():
    """Play a single round of the guessing game."""
    low, high, max_attempts = get_difficulty()
    target = random.randint(low, high)

    attempts = 0
    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        guess = get_guess(low, high)
        attempts += 1

        if guess == target:
            print(f"\nCorrect! You guessed it in {attempts} attempt(s).")
            return
        elif guess < target:
            print("Too low!")
        else:
            print("Too high!")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts remaining: {remaining}\n")

    print(f"\nOut of attempts! The number was {target}.")


def main():
    print("=" * 40)
    print("      WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 40)

    while True:
        play_round()

        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
