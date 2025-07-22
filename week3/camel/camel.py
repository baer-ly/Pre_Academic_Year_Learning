# prompt for camel case -> firstName
# Return snake case -> first_name

# Create empty string to use for display and avoid any confusion.
# loop through user input
# check case of each character
# when the character is lowercase add it to 

def generate_case(text: str) -> str:
    gen_string = ""
    for char in text:
        if char.islower():
            gen_string += char
        elif char.isupper():
            gen_string += char.replace(char,"_" + char.lower())

    return gen_string


def main():
    user_text = input("camelCase: ")
    print(f"snake_case {generate_case(user_text)}")

main()