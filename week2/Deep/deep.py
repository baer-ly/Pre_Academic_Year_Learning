def deep_thought():
    # """
    # This function will prompt the user to answer the ultimate question of life, the universe, and everything.
    # -> If the user answers with '42','forty-two' or 'forty two' it will print a congratulatory message.
    # -> If the user answers with anything else, it will print a message indicating that the answer is incorrect.
    # """
    ctrl = True
    while ctrl:
        answer = input("What is the answer to the ultimate question of life, the universe, and everything?\n").strip().lower()
        if answer in ['42', 'forty-two', 'forty two', '42.0']:
            print("Yes")
            ctrl = False
        else:
            print("No")
# example usage of the function
deep_thought()