Xw = input("Enter your Score:")
guess = ""
chances = 0
limit = 3
limitReach = False

while guess != Xw and not(limitReach):
    if chances < limit:
        guess = input("Guess Your Score:")
        chances += 1
    else:
        limitReach = True

if limitReach:
    print("You Loose! Try Tomorrow")
else:
    print("You Win!")