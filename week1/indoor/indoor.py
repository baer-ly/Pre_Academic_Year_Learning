def indoor_voice(text: str) -> str:
    # Convert a string to an indoor voice by replacing all uppercase letters with lowercase letters.
    # :param text: The input string to convert.
    # :return: The converted string in lowercase.
    return text.lower()

text = input("Enter a string to convert to indoor voice: ")
print(indoor_voice(text))
# Example usage:
# print(indoor_voice("HELLO WORLD"))  # Output: "hello world"
# print(indoor_voice("Python is FUN!"))  # Output: "python is fun!"
# print(indoor_voice("Indoor Voice"))  # Output: "indoor voice"
# print(indoor_voice("12345"))  # Output: "12345" (numbers are unaffected)