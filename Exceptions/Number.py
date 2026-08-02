# x = int (input("Enter x: "))
# print("x is", x)

# try:
#     x = int (input("Enter x: "))
#     print(f"x is {x} {x}")
# except ValueError:
#     print("x is not an integer.")


# Throwing an exception when the input is not an integer also throws an error in wrong case
# try:
#     x = int (input("Enter X: "))
# except ValueError:
#     print("x is not an integer.")

# print(f"x is {x}")

# correct way to throw an exception when the input is not an integer
# try:
#     x = int (input("Enter X: "))
# except ValueError:
#     print("x is not an integer.")
# else:
#     print(f"x is {x}")

#while loop to keep asking for input until the user enters an integer
# while True:
#     try:
#         x = int (input("Enter X: "))
#     except ValueError:
#         print("x is not an integer.")
#     else:
#         break

# print(f"x is {x}")

# logical break statement to break the loop when the user enters an integer
# while True:
#     try:
#         x = int (input("Enter X: "))
#         break
#     except ValueError:
#         print("x is not an integer.")
    
# print(f"x is {x}")


def main():
    x = abc("Enter X: ")
    print(f"x is {x}")

def abc(a):
    while True:
        try:
            return int (input(a))
        except ValueError:
            pass

main()