def get_user_name():
    user_name = input("Assistant: Hi! I'm Mini Alexa. What's your name?\nYou: ")
    return user_name

def build_greeting(user_name):
    """Create a personalized greeting."""
    return (
        f"Assistant: Nice to Meet You, {user_name}!\n"
        "Assistant: Type 'help' later to see what I can do."
    )