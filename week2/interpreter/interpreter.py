# basic arithmetic calculator
# In the format of x y x -> x is int, y is operation

def basic_math(text: str):
    # expect input to be in the correct format
    # create a list of operations to check if its a valid operation
    format_text = text.split()
    opp = format_text[1]
    num1 = float(format_text[0])
    num2 = float(format_text[2])
    if opp == "+":
        answer = num1 + num2
        return answer
    elif opp == "/":
        answer = num1 / num2
        return answer
    elif opp == "*":
        answer = num1 * num2
        return answer
    elif opp == "-":
        answer = num1 - num2
        return answer
    else:
        return "incorrect input"

    # print(answer)

def main():
    user_input = input("Expression: ")
    print(basic_math(user_input))

main()
# num = "25 + 12"
# print(int(num))