a = float(input("Enter the first number: "))
operator = input("Enter the operator: ")
b = float(input("Enter the second number: "))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0:
        print("Error: Division by zero is not allowed.")
    elif (a % b) == 0:
        print(a // b)
    else:
        print(a / b)  
elif operator == "%":
    print(a % b)
elif operator == "**":
    print(a ** b)
else:
    print("Operator is invalid")