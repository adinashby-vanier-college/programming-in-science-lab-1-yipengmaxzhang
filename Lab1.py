# Function 1: Write a simple Hello World program
# This function should print "Hello, World!" to the screen.
def hello_world():
    print("Hello, World!")

# Function 2: Get input and output with different variable types
# This function should prompt the user for their name (string), age (int), and height (float),
# and then print them back in a formatted message.
def input_output():
    name = input("Hello! What is your name?: ")
    age = int(input("What is your age: "))
    height = float(input("How tall are you, in feet?: "))
    print("Welcome, " + name + ", you are " + str(age) + " years old and you are " + str(height) + " feet tall!")
