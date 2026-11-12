score = int(input("Enter the score of Jemi: "))
balls = int(input("Enter the number of balls faced by Jemi: "))

# if, elif, and else statement with nested if statement in Python.
if score >= 100:
    print("Whoo! Jemi scored a century!")
    if balls <= 100:
        print("Jemi scored a quick century with strike rate of", (score/balls)*100)
    else:
        print("Jemi scored a slow century with strike rate of", (score/balls)*100)
elif score >= 50:
    print("Jemi scored a half-century!")
else:
    print("Jemi did not score well.")

# And statement in Python.
if score >= 100 and balls <= 100:
    print("Jemi scored a quick century with strike rate of", (score/balls)*100)
elif score >= 100 and balls > 100:
    print("Jemi scored a slow century with strike rate of", (score/balls)*100)
elif score >= 50 and balls <= 50:
    print("Jemi scored a quick half-century with strike rate of", (score/balls)*100)
elif score >= 50 and balls > 50:
    print("Jemi scored a slow half-century with strike rate of", (score/balls)*100)
else:
    print("Jemi did not score well.")

# Or statement in Python.
if score >= 30 or balls >= 50:
    print("Jemi played a decent innings with a strike rate of", (score/balls)*100)
else:
    print("Jemi did not play well.")

# Not statement in Python.
if score >= 100:
    print("Jemi scored a century!")
if not score >= 100:
    print("Jemi did not score a century.")