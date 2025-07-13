"""
CP1404/CP5632 Practical - Client code to use the Car class.
"""

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    # Create limo with 100 fuel
    limo = Car("Limo", 100)

    # Add 20 fuel
    limo.add_fuel(20)

    # Print fuel
    print(f"{limo.name} has fuel: {limo.fuel}")

    # Attempt to drive 115 km
    limo.drive(115)

    # Print car (tests __str__)
    print(limo)


main()
