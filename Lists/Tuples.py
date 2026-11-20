# Tuples are immutable data structures
jersey_numbers = (5, 31, 64, 19, 27, 18, 13) # Tuple of jersey numbers

# jersey_numbers[9] = 32 # This will raise an error because tuples are immutable

print(jersey_numbers) # Printing the tuple of jersey numbers

# Tuples inside lists
women_cricketers = [("Jemimah Rodrigues", 5), ("Shreyanka Patil", 31), ("Alice Capsey", 64), ("Sophie Ecclestone", 19), ("Alana King", 27), ("Smriti Mandhana", 18)] # List of tuples containing women cricketers and their jersey numbers

women_cricketers.append(("Tahlia Mcgrath", 32)) # Adding a new tuple to the list
women_cricketers.remove(("Smriti Mandhana", 18)) # Removing a tuple from the list
women_cricketers.pop(5) # Removing the tuple at index 5

print(women_cricketers) # Printing the updated list of tuples containing women cricketers and their jersey numbers