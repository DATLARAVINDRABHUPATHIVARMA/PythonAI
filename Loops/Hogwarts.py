# team = ["Sruthi", "Sravani", "Radha", "Suneel", "Rangavathi", "Maharathi Ravindra"] #keys
# power = ["The Great Highness", "Princess", "The Giant Queen", "King", "Wise Queen Mom", "The Strongest Warrior General of the Army"] #values

# print(team[0])
# print(team[1])
# print(team[2])


# for x in team:
#     print(x)

# for _ in team:
#     print(_)

# for team in team:
#     print(team)

# for x in range(len(team)):
#     print(x, team[x])

# for x in range(len(team)):
#     print(x+1, team[x])

# kingdom = { "Sruthi" : "The Great Highness" , "Sravani" : "Princess" , "Radha" : "The Giant Queen" , "Suneel" : "King" , "Rangavathi" : "Wise Queen Mom" , "Maharathi Ravindra" : "The Strongest Warrior General of the Army" }

# print(kingdom)
# print(kingdom["Radha"])
# print(kingdom["Sruthi"])
# print(kingdom["Sravani"])
# print(kingdom["Suneel"])
# print(kingdom["Rangavathi"])
# print(kingdom["Maharathi Ravindra"])

# for x in kingdom:
#     print(x, kingdom[x], sep=", ")

royalpalace = [ {"name":"Sruthi", "role":"The Great Highness", "weapon":"Highness Crown"}, {"name":"Sravani", "role":"Princess", "weapon":None}, {"name":"Radha", "role":"The Giant Queen", "weapon":"Queen Royal Sword"}, {"name":"Suneel", "role":"King", "weapon":"Strongest Mace"}, {"name":"Rangavathi", "role":"Wise Queen Mom", "weapon":"Protection Shield"}, {"name":"Maharathi Ravindra", "role":"The Strongest Warrior General of the Army", "weapon":"Immortal Visionary Bow and Shields"}]

for a in royalpalace:
    print(a["name"], "is", a["role"], "of our Royal Kingdom. Uses", a["weapon"], "as the weapon")