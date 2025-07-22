# Prompt for time 24h or 12h format {00:00, 0:00}
# Breakfast -> 7:00 to 8:00 (inclusive of the boundaries)
# Lunch -> 12:00 to 13:00 (inclusive of the boundaries)
# Dinner -> 18:00 to 19:00 (inclusive of the boundaries)


def main():
    # Assume user input 24h format
    user_time = input("What time is it: ")
    # split_time = user_time.split(":")
    # Convert to float for easier comparison
    meal_time = convert(user_time)

    if meal_time >= 7 and meal_time < 8.01:
        print('Breakfast time')
    elif meal_time >= 12 and meal_time < 13.01:
        print('Lunch time')
    elif meal_time >= 18 and meal_time < 19.01:
        print('Dinner time')
    else:
        print()
    # Assume 12h format with thee correct 'a.m.'/ 'p.m.'

    user_time_12h = input("What time is it: ").lower().split()
    meal_time_12h = convert(user_time_12h[0])
    if user_time_12h[1] =='a.m.':
        if meal_time_12h >= 7 and meal_time_12h < 8.01:
            print('Breakfast time')
    elif user_time_12h[1] =='p.m.':
        if meal_time_12h >= 12 and meal_time_12h <= 1.01:  #This one doesnt work well...
            print('Lunch time')
        elif meal_time_12h >= 6 and meal_time_12h <= 7.01:
            print('Dinner time')
        else:
            print()

def convert(time: str):
    # assume 24h
    check_time = time.split(":")
    minutes = float(check_time[1])
    hours = float(check_time[0])
    time_f = float(hours + (minutes / 60))
    return time_f

    


if __name__ == "__main__":
    main()