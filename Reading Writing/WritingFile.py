em_file = open("sample.txt","w") # Overwrite on the same file or write on a new file
em_file.write("Sruthi - Royal Princess Highness" "\tSruthi - Royal Princess Highness")

em_file.close()

# a - used to append on the existing file

# Sample EVEN ODD new file created
emp_fil = open("EvenOdd.py","w")
emp_fil.write("n = int(input(\"Enter a Number:\"))\n\nif n%2 == 0:\n\tprint(f\"{n} is Even Number\")\nelse:\n\tprint(f\"{n} is Odd Number\")")