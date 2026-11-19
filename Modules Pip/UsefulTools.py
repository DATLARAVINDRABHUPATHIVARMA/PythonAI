import random

feetPerMile = 5280
mKm = 1000
SoccerPlayers = [ "Messi", "Ronaldo", "Cubarsi", "Pogba", "Ter Stegen", "Donaruma" ]

def get_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)