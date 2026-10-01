from datetime import datetime

def recommend_activity():
    """
    Recommend an activity based on the current time.

    This is a rule-based AI demonstration.
    The system uses predefined if/elif/else rules
    instead of a trained machine learning model.
    """
    current_hour = datetime.now().hour

    if current_hour < 12:
        activity = "Good Morning! It's a good time for breakfast and planning your day."
    elif current_hour < 17:
        activity = "Good Afternoon! It's a good time to work or study."
    elif current_hour < 21:
        activity = "Good Evening! It's a good time to relax or go for a walk."
    else:
        activity = "It's late. A good time to relax and prepare for sleep."
    return activity

def perceptron_demo(input1, input2):
    """
    Demonstrates a simplified artificial neuron.

    Inputs are multiplied by weights, a bias is added,
    and a step activation function produces 0 or 1.
    """
    weight1 = 0.5
    weight2 = 0.5

    bias = -0.5

    weighted_sum = (input1 * weight1) + (input2 * weight2) + bias

    if weighted_sum > 0:
        output = 1
    else:
        output = 0

    return output