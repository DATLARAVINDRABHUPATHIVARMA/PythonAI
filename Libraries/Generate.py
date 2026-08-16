#whole random module import
import random

coin = random.choice( [ "Heads", "Tails" ] )
print(coin)



# Limited random module import using "from" keyword
# from random import choice

# dice = choice( [ 1, 2, 3, 4, 5, 6 ] )
# print(dice)

number = random.randint(0, 100)
# print(number)

cards = [ "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King" ]
random.shuffle(cards)
print(cards)