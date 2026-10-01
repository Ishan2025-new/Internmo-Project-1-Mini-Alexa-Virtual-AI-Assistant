import random

def play_guessing_game():
    """Run the Number Guessing Game"""
    secret_number = random.randint(1, 20)
    max_attempt = 5

    print("\nAssistant: I'm thinking of a number between 1 and 20.")
    print(f"Assistant: You have {max_attempt} attempts.")

    for attempt in range(1, max_attempt + 1):
        try:
            guess = int(input(f"You (Attempt {attempt}): "))

            if guess == secret_number:
                print("Assistant: Congratulations! You guessed the number!")
                return
            elif guess < secret_number:
                print("Assistant: Higher!")
            else:
                print("Assistant: Lower!")
        except ValueError:
            print("Assistant: Please enter a valid number.")

    print(f"Assistant: Sorry, you used all {max_attempt} attempts."
          f"The Answer was {secret_number}.")