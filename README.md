# Virtual AI Assistant (Mini Alexa)

A simple command-line virtual assistant inspired by Alexa. This project is a beginner-friendly Python application that greets the user, responds to basic commands, performs calculations, tells jokes and facts, plays a number guessing game, and demonstrates AI-inspired logic.

## Features

- Personalized greeting using the user's name
- Shows the current time and date
- Performs simple arithmetic operations
- Provides random motivational quotes, jokes, and facts
- Plays a number guessing game
- Suggests activities based on the current time
- Demonstrates a simplified perceptron logic function
- Includes a help menu with all available commands

## Project Structure

- `main.py` - Main program loop and command handling
- `greetings.py` - Greeting logic
- `datetime_utils.py` - Date and time utilities
- `calculator.py` - Arithmetic functions
- `content.py` - Quotes, jokes, and fun facts
- `game.py` - Number guessing game
- `ai_concepts.py` - Activity recommendation and perceptron demo
- `help_menu.py` - Help menu output

## How to Run

From the project folder, run:

```bash
python main.py
```

If you are using the included virtual environment, activate it first:

```bash
internmo_project1\Scripts\activate
python main.py
```

## Available Commands

Once the assistant starts, you can type the following commands:

- `help` - View the help menu
- `time` - Show the current time
- `date` - Show the current date
- `calculate` - Perform a math operation
- `quote` - Get a random quote
- `joke` - Tell a joke
- `fact` - Show a random fact
- `game` - Play the number guessing game
- `recommend` - Get an activity recommendation
- `perceptron` - Run a perceptron demonstration
- `hi`, `hello`, `hey` - Friendly greeting
- `exit`, `quit`, `bye` - Exit the assistant

## Example

```text
Assistant: Hi! I'm Mini Alexa. What's your name?
You: Alice
Assistant: Nice to Meet You, Alice!
Assistant: Type 'help' later to see what I can do.

Alice: time
Assistant: The current time is 10:25:00 AM.

Alice: calculate
Assistant: Enter the first number: 10
Assistant: Enter operator (+, -, *, /): +
Assistant: Enter the second number: 5
Assistant: 15.0
```

## Notes

This project is designed for learning and experimentation. It uses simple rule-based logic rather than a full AI system, making it a great beginner project for understanding Python, user input handling, and basic AI concepts.
