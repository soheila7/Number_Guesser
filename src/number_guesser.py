import random

def validate_input(user_guess: str) -> bool:
    """
    Validates the user's input to ensure it is a digit within the range 1 to 100.

    Args:
        user_guess (str): The user's guess as a string.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    if not user_guess.isdigit():
        print("Invalid input")
        return False
    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1:
        print("Invalid input")
        return False
    
    return True


def main() -> None:
    """
    Main function to execute the number guessing game. 
    The user guesses a random number between 1 and 100.
    """
    rand_num: int = random.randint(1, 100)
    score: int= 100

    while True:
        user_guess: str = input("Guess a number between 1 and 100: ")

        if user_guess == "q":
            print("Thank you for playing, Goodbye!")
            break

        if not validate_input(user_guess):
            continue

        user_guess = int(user_guess)
        if rand_num > user_guess:
            print("your guess is too low")
        elif rand_num < user_guess:
            print("your guess is too high")
        else:
            print("your guess is correct!")
            print("Your score is:" , score)
            break

        score -= 10
        score = max(score , 0)


if __name__ == "__main__":
    main()
