def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    # TODO: Convert d (a string) to a float representing dollars
    return float(d.strip('$'))

def percent_to_float(p: str) -> float:
    # TODO: Convert p (a string) to a float representing a percentage
    return float(p.strip('%')) / 100

main()