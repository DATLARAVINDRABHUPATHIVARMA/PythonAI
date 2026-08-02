# print("#")
# print("#")
# print("#")

# for _ in range(7):
#     print('#')

# def tab():
#     print_col(2)

# def print_col(c):
#     for i in range(c):
#         print("#")

# without using for loop height
# def print_col(r):
#     print("#\n" * r, end="")

def tab():
    print_square(20)
    # print_row(4)

# Width of the row
# def print_row(x):
#     print("?" * x, end="")

# def print_square(Size):
    # for each row in the square
#     for i in range(Size):
#         print("#" * Size)
        # for each brick in the row
        # for j in range(Size):
        #     # print brick
        #     print("#", end="")
        # print()

def print_square(Size):
    for i in range(Size):
        print_row(Size)

def print_row(x):
    print("ui " * x)

tab()