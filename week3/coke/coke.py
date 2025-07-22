# Prompt user to insert coins, [25, 10, 5]
# until total input >= 50
# If total_input > 50 display the amount owed to the user
def coke():
    payable = -50
    valid_coins = [25, 10, 5]
    while True:
        print(f"Amount due: {abs(payable)}")
        print()
        amount_paying = int(input("Amount due: "))
        if amount_paying in valid_coins:
            payable += amount_paying
            if payable >= 0 :
                print(f"Change Owed: {payable}")
                break
            
coke()