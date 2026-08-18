import sys

# print(sys.argv[1])

# try:
#     print(sys.argv[1])
# except IndexError:
#     print("Please provide a valid integer argument.")

# if len(sys.argv) == 1:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

print("Hello, my name is", sys.argv[1], "and I am the", sys.argv[2], "of the Royal Kingdom" )

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)