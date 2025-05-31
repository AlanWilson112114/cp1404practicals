def main():
    """Temperature conversion between Celsius (C) and Fahrenheit (F)"""
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to = float(input("Celsius: "))
            from_fahrenheit = convert_celsius_to_fahrenheit(celsius_to)
            print(f"Result: {from_fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit_to = float(input("Fahrenheit: "))
            from_celsius = convert_fahrenheit_to_celsius(fahrenheit_to)
            print(f"Result: {from_celsius:.2f} C")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()
