
emp_file = open("sample.txt","r")
# print(emp_file.readable())
# print(emp_file.read())
# print(emp_file.readlines()[2])

# Using for loop to readlines
for a in emp_file.readlines():
    print(a)

emp_file.close()