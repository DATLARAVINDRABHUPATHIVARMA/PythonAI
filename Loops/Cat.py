print("Hello, Yuvarani Sruthi")
print("Hello, Yuvarani Sruthi")
print("Hello, Yuvarani Sruthi")
print("Hello, Yuvarani Sruthi")


# while loop
# i = 7
# while i != 4:
#     print("Hello, Yuvarani Sruthi Om Sai Varma")
#     i = i-1

i = 0
while i < 5:
    print("Hello, Yuvarani Sruthi Om Sai Varma")
    i += 1

# for loop list
for i in [0,1,2,4]:
    print("Hello, Maharani Radha")

# for loop range
for _ in range(5):
    print("Hello, Maharani Sruthi Om Sai Varma")

# Multiplication of String
# print("Hello, Yuvarani Sruthi Om Sai Varma" * 5)

print("Hello, Yuvarani Sruthi Om Sai Varma\n" * 5)
print("Hello, Maharani Radha\n" * 5, end=" ")

# while True:
#     n = int(input("Enter a number: "))
#     if n < 0:
#         continue
#     else:
#         break

# for n in range(n):
#     print("Hello, Radha Maharani")

while True:
    n = int(input("Enter a number: "))
    if n > 0:
        break

for n in range(n):
    print("Hello, Radhey")

# function loop
def yuva():
    num = getnumber()
    rani(num)

def getnumber():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            break
    return n
    
def rani(n):
    for i in range(n):
        print("Hello, Yuvarani Sruthi Om Sai Varma")

yuva()