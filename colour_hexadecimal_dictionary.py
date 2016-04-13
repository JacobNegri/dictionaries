# asks for a colour and returns its hexadecimal value

COLOUR_NAMES = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AZURE1": "#f0ffff", "BLACK": "#000000",
                "BEIGE": "#f5f5dc", "BROWN": "#a52a2a", "BLUE1": "#0000ff"}

# print(COLOUR_NAMES)
colour = input("Enter colour to find hexadecimal value: ").upper()
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour choice!")
    colour = input("Enter colour to find hexadecimal value: ").upper()