name = input("What is your name? ")

# conditional statements using if, elif & else
if name == "Sruthi":
    print("Rani")
elif name == "Radha":
    print("Rani")
elif name == "Sravani":
    print("Rani")
elif name == "Suneel":
    print("Raja")
elif name == "Rangavathi":
    print("Rani")
elif name == "Ravindra":
    print("Sarva Sainyadhyaksha")
else:
    print("Unknown")


# 'or' keyword
if name == "Sruthi" or name == "Radha" or name == "Sravani" or name == "Rangavathi":
    print("Rani")
elif name == "Suneel":
    print("Raja")
elif name == "Ravindra":
    print("Sarva Sainyadhyaksha")
else:
    print("Unknown")


# match case statement
match name:
    case "Sruthi":
        print("Rani")
    case "Radha":
        print("Rani")
    case "Sravani":
        print("Rani")
    case "Suneel":
        print("Raja")
    case "Rangavathi":
        print("Rani")
    case "Ravindra":
        print("Sarva Sainyadhyaksha")
    case _:
        print("Unknown")


# Code Shorten in match case statement
match name:
    case "Sruthi" | "Radha" | "Sravani" | "Rangavathi":
        print("Rani")
    case "Suneel":
        print("Raja")
    case "Ravindra":
        print("Sarva Sainyadhyaksha")
    case _:
        print("Unknown")