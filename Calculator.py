# x = int(input("What's X? "))
# y = int(input("What's Y? "))

# print(f"The sum of {x} and {y} is {x + y}")
# print(f"The difference of {x} and {y} is {x - y}")
# print(f"The product of {x} and {y} is {x * y}")
# print(f"The quotient of {x} and {y} is {x // y}")
# print(f"The remainder of {x} and {y} is {x % y}")

a = round(float(input("What's A? ")), 5)
b = round(float(input("What's B? ")), 5)


print(f"The sum of {a} and {b} is {round(a + b, 3)}")
print(f"The difference of {a} and {b} is {round(a - b, 3)}")
print(f"The product of {a} and {b} is {round(a * b, 3)}")
print(f"The quotient of {a} and {b} is {round(a / b, 3)}")
print(f"The remainder of {a} and {b} is {a % b}")

c = round(a + b, 4)
print(f"The sum of {a} and {b} is {c}")