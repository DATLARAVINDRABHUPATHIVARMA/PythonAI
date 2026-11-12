women_cricketers = ["Jemimah Rodrigues", "Shreyanka Patil", "Harmanpreet Kaur", "Smriti Mandhana", "Harleen Deol", "Richa Ghosh"] # List of women cricketers
jersey_numbers = [5, 31, 23, 18, 33, 13] # List of jersey numbers

# print(women_cricketers)
# print(jersey_numbers)

# extend function is used to add multiple elements to the end of a list
women_cricketers.extend(["Alana King", "Alice Capsey", "Sophie Ecclestone"]) # Adding multiple elements to the list
jersey_numbers.extend([27, 64, 19]) # Adding multiple elements to the list

# append function is used to add a single element to the end of a list
women_cricketers.append("Tahlia Mcgrath") # Adding a single element to the list
jersey_numbers.append(32) # Adding a single element to the list

# insert function is used to add an element at a specific index in a list
women_cricketers.insert(2, "Nat-Sciver Brunt") # Adding an element at index 2
jersey_numbers.insert(2, 39) # Adding an element at index 3

# remove function is used to remove an element from a list
women_cricketers.remove("Harmanpreet Kaur") # Removing an element from the list
jersey_numbers.remove(23) # Removing an element from the list

# clear function is used to remove all elements from a list
# jersey_numbers.clear() # Removing all elements from the list

# pop function is used to remove an element from a specific index in a list
women_cricketers.pop(2) # Removing an element from index 2
jersey_numbers.pop(2) # Removing an element from index 2

# index function is used to find the index of an element in a list
# print(women_cricketers.index("Smriti Mandhana")) # Finding the index of an element in the list

# count function is used to find the number of occurrences of an element in a list
# print(women_cricketers.count("Smriti Mandhana")) # Finding the number of occurrences of an element in the list

# sort function is used to sort the elements of a list in ascending order
jersey_numbers.sort() # Sorting the list in ascending order

# reverse function is used to reverse the order of elements in a list
# women_cricketers.reverse() # Reversing the order of elements in the list

# copy function is used to create a copy of a list
women_cricketers_copy = women_cricketers.copy() # Creating a copy of the list

print(women_cricketers) # Printing the updated list of women cricketers
print(jersey_numbers) # Printing the updated list of jersey numbers
print(women_cricketers_copy) # Printing a copy of the list of women cricketers