def greeting(text : str) -> str:
    # """
    # Prompts user for a greeting.
    # if greeting starts with 'hello', -> Output: $0
    # if greeting starts with an 'h'( but not 'hello'), -> Output: $20
    # Otherwise, -> Output: $100
    # """
    if text.startswith('hello'):
        return "0"
    elif text.startswith('h'):
        return "20"
    else:
        return "100"
# Example usage of the greeting function
def main():
    user_input = input("Greeting: ").lower()
    result = greeting(user_input)
    print(f"The output is: ${result}")
main()