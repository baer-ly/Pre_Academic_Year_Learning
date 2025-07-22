# prompt for a string
# return the same text without the vowels

def tweet(text: str):
    lower_vowels = ["a", "e", "i", "o", "u"]
    upper_vowels = ["A", "E", "I", "O", "U"]
    outText = ""
    for char in text:
        if char in lower_vowels or char in upper_vowels:
            pass
        else:
            outText += char
    return outText
    
def main():
    user_text = input("Input: ")
    print(tweet(text = user_text))

main()

# I used list comprehension to find specific characters in a string
# If the character is found in the original string we just pass over it as it has no value to us
# every other character is then added to an empty string as strings are immutable
