from greetings import get_user_name, build_greeting
from datetime_utils import get_current_date, get_current_time
from calculator import calculate
from content import get_random_quotes, get_random_joke, get_random_fact
from game import play_guessing_game
from ai_concepts import recommend_activity, perceptron_demo
from help_menu import print_help

def handle_calculator():
    """Get two numbers and an operator, then calculate the result."""

    try:
        num1 = float(input("Assistant: Enter the first number: "))
        operator = input("Assistant: Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Assistant: Enter the second number: "))

        result = calculate(num1, operator, num2)

        print("Assistant:", result)

    except ValueError:
        print("Assistant: Please enter valid numbers.")


def handle_perceptron():
    """Run the simplified perceptron demonstration."""

    try:
        input1 = float(input("Assistant: Enter input 1: "))
        input2 = float(input("Assistant: Enter input 2: "))

        result = perceptron_demo(input1, input2)

        print("Assistant: Perceptron output:", result)

    except ValueError:
        print("Assistant: Please enter valid numeric inputs.")


def run_assistant():
    """Start and run the Mini Alexa assistant."""

    print("=" * 50)
    print("          MINI ALEXA - VIRTUAL AI ASSISTANT")
    print("=" * 50)

    # Get and store user's name
    user_name = get_user_name()

    print()
    print(build_greeting(user_name))
    print()

    # Main command loop
    while True:

        try:
            user_input = input(f"{user_name}: ").strip().lower()

        except (KeyboardInterrupt, EOFError):
            print(f"\nAssistant: Goodbye, {user_name}!")
            break

        # Ignore empty input
        if not user_input:
            print("Assistant: Please enter a command. Type 'help' for available commands.")
            continue

        # Exit command
        if user_input in ["exit", "quit", "bye"]:
            print(f"Assistant: Goodbye, {user_name}! Have a great day.")
            break

        # Help command
        elif user_input == "help":
            print_help()

        # Time command
        elif user_input == "time" or "time" in user_input:
            print(f"Assistant: The current time is {get_current_time()}.")

        # Date command
        elif user_input == "date" or "date" in user_input:
            print(f"Assistant: Today's date is {get_current_date()}.")

        # Calculator command
        elif user_input == "calculate" or user_input.startswith("calculate"):
            handle_calculator()

        # Quote command
        elif "quote" in user_input:
            print("Assistant:", get_random_quotes())

        # Joke command
        elif "joke" in user_input:
            print("Assistant:", get_random_joke())

        # Fact command
        elif "fact" in user_input:
            print("Assistant:", get_random_fact())

        # Guessing game
        elif user_input == "game" or "game" in user_input:
            play_guessing_game()

        # Rule-based recommendation
        elif "recommend" in user_input:
            print("Assistant:", recommend_activity())

        # Perceptron demonstration
        elif "perceptron" in user_input:
            handle_perceptron()

        # Simple greeting
        elif user_input in ["hi", "hello", "hey"]:
            print(f"Assistant: Hello, {user_name}! How can I help you?")

        # Unknown command
        else:
            print(
                "Assistant: I'm not sure I understood that. "
                "Type 'help' to see what I can do."
            )

if __name__ == "__main__":
    run_assistant()