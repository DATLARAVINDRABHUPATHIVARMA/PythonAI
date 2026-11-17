# number = int(input("Enter a Number: "))
# print(number)

# try and except is used in error cases
# try:
#     num = int(input("Enter a Number: "))
#     print(num)
# except:
#     print('Invalid input')

# Advanced Except Cases Zero with other type of errors
try:
    b = 34/0
    a = int(input("Enter a Number: "))
    print(a)
except ValueError: #ValueError also inbuilt keyword for except case
    print("Invalid input")
except ZeroDivisionError as err: #ZeroDivisionError is inbuilt keyword for except case
    print(err)