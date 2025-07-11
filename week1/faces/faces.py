def convert(text: str) -> str:
    # This function takes a string with "old emoji" and replaces it with "new emoji".
    # :param text: The input string to be modified.
    # :return: The modified string with "new emoji" replacing "old emoji".
    return text.replace(":)", "🙂").replace(":(", "🙁").replace(":D", "😄").replace(";)", "😉")

def main():
    # Example usage of the convert function
    text = input("Enter a string with old emojis (e.g., :), :(, :D): ")
    print("Converted text:", convert(text))

main()