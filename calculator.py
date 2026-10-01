def calculate(num1, num2, operator):
    try:
        if operator == "+" or operator == "add":
            return num1 + num2
        elif operator == "-" or operator == "subtract":
            return num1 - num2
        elif operator == "*" or operator == "multiply":
            return num1 * num2
        elif operator == "//" or operator == "divide":
            if num2 == 0:
                return "I can't divide a number -- try a different number"
            return num1 // num2
        else:
            return "Invalid Operator. Please use +, -, * or /."
    except Exception as e:
        return "Sorry, I couldn't perform that calculation."