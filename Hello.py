print("Hello, World")
name = input("What's your Name?").strip().title()
Defo, first, last = name.split("/")

print(f"Hello {Defo}", first +f" {last}, You are the greatest person in the world")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()