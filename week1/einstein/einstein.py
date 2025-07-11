def einstein(mass: float) -> float:
    # This function calculates the energy equivalent of a given mass using Einstein's equation E=mc^2.
    # :param mass: The mass in kilograms.
    # :return: The energy in joules.
    c = 299792458  # Speed of light in m/s
    return mass * c ** 2

def main():
    # Example usage of the einstein function
    mass = int(input("Enter mass in kilograms: "))  # Mass in kilograms
    energy = einstein(mass)
    print(f"The energy equivalent of {mass} kg is {energy} joules.")

main()