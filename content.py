import random

QUOTES = [
    "Believe in yourself and keep moving forward.",
    "Success comes from consistent effort.",
    "Every expert was once a beginner.",
    "Small progress is still progress.",
    "Learning never stops."
]

JOKES = [
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why was the computer cold? Because it left its Windows open.",
    "Why did the developer go broke? Because he used up all his cache.",
    "What do programmers say when they make a mistake? It wasn't a bug, it was a feature."
]

FACTS = [
    "Python was named after Monty Python.",
    "The first computer mouse was made of wood.",
    "The human brain contains billions of neurons.",
    "The Earth is approximately 4.5 billion years old.",
    "Water covers about 71 percent of Earth's surface."
]

def get_random_quotes():
    """Return a random motivational quotes"""
    return random.choice(QUOTES)

def get_random_joke():
    """Return a random joke"""
    return random.choice(JOKES)

def get_random_fact():
    """Return a random fact."""
    return random.choice(FACTS)