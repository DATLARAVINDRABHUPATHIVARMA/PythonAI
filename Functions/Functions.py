# Creating a basic function to print hello 

def hello(name):
    print("Hello " + name)

def goodbye():
    print("Goodbye, Raja!")
    print("Goodbye, Rani!") 


# function inside a function and parameter passing 
def main(name, age):
    hello(name)
    print("You are " + str(age) + " years old.")

main("Raja", '30')
