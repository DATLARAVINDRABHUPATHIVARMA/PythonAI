x = int (input("Enter x: "))

# using Modulus symbol to check if the number is even or odd in a simple way
if x % 2 == 0:
    print("Even")
else:
    print("Odd")



# using main function and complex function
def main():
    x = int(input("Enter x: "))

    # using Modulus symbol to check if the number is even or odd in a simple way
    if even(x):
        print("Even")
    else:
        print("Odd")

def even(n):
    return n % 2 == 0 

main()


# using main function and complex function & boolean return type
def main():
    x = int(input("Enter x: "))

    # using Modulus symbol to check if the number is even or odd in a simple way
    if even(x):
        print("Even")
    else:
        print("Odd")

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()


# Pythonic way of checking if the number is even or odd using main function and complex function & boolean return type
def main():
    x = int(input("Enter x: "))

    if even(x):
        print("Even")
    else:
        print("Odd")

def even(n):
    return True if n % 2 == 0 else False

main()