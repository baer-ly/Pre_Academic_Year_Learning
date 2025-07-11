def playback(text :str) -> str:
    # This function takes a string input and returns it with  "..." added between each word.

    # :param text: The input string to be returned.
    # :return: The same input string.
    return '...'.join(text.split())

# Example usage:
# print(playback("Hello World"))  # Output: "Hello...World"
# print(playback("Python is fun!"))  # Output: "Python...is...fun!"
# print(playback("Playback function"))  # Output: "Playback...function"
# print(playback("12345"))  # Output: "12345" (numbers are unaffected)
# print(playback("Hello...World"))  # Output: "Hello...World"
text = input("Enter a string to playback: ")
print(playback(text))  # Output: The input string with "..." between each word.