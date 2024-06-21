"""
Hexadecimal Colour Code Lookup Program
"""

# Dictionary of colour names to hex codes
COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

# Create a lowercase version of COLOUR_TO_HEX
lowercase_colour_to_hex = {colour.lower(): hex_value for colour, hex_value in COLOUR_TO_HEX.items()}

# Input loop to get colour
colour_name = input("Enter colour name (blank to stop): ").lower()

while colour_name != "":
    if colour_name in lowercase_colour_to_hex:
        hex_code = lowercase_colour_to_hex[colour_name]
        print(f"{colour_name.capitalize()} is {hex_code}")
    else:
        print("Invalid colour name")

    colour_name = input("Enter colour name (blank to stop): ").lower()
