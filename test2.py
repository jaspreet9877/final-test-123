COLORS = {
    "red": {"name": "RED", "secondary": {"blue": "PURPLE", "yellow": "ORANGE"}},
    "blue": {"name": "BLUE", "secondary": {"red": "PURPLE", "yellow": "GREEN"}},
    "yellow": {"name": "YELLOW", "secondary": {"red": "ORANGE", "blue": "GREEN"}}
}

color1 = input("Enter the first color: ").lower()
color2 = input("Enter the second color: ").lower()

# Checking for valid color
if color1 not in COLORS:
    print("Error: Invalid Color1")
elif color2 not in COLORS:
    print("Error: Invalid Color2")
elif color1 == color2:
    print("Error: The two colors you entered are same")
else:

    secondary_color = COLORS[color1]["secondary"][color2]
    print(f"The secondary color is {secondary_color}")
