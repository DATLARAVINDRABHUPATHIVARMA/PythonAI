# Uppercase Function
Queen = "Radha Maharani"
print(Queen.upper() + " is Queen of the Kingdom")

# Lowercase Function
print(Queen + " is Queen of the Kingdom".lower())

# Boolean Functions
print(Queen.islower())

# Combinations Functions
print(Queen.upper().isupper())

# Length of string
print(len(Queen))

# Indexing of string
print(Queen[0])
print(Queen[1])
print(Queen[2:4])

# Index Function
print(Queen.index("dha Mahar"))

# Index Substring Not Found
# print(Queen.index("Maharaja")) # This will throw an error because the substring is not found in the string

# Replace Function
print(Queen.replace("Radha", "Highness Sruthi"))