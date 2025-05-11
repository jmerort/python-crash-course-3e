"""
7-6
Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.

May 2025
@jmerort

I will modify excercise 7.4
"""


# Version 1

"""
topping = ''

while topping != 'quit':
    topping = input("Enter a topping or enter 'quit' to continue: ")
    if topping == 'quit':
        print("Done. Enjoy your pizza!")
    else:
        print(f"{topping.title()} added to your pizza.")
"""


# Version 2

"""
active = True # flag variable
topping = ''

while active:
    topping = input("Enter a topping or enter 'quit' to continue: ")
    if topping == 'quit':
        print("Done. Enjoy your pizza!")
        active = False
    else:
        print(f"{topping.title()} added to your pizza.")
"""


# Version 3

topping = ''

while True:
    topping = input("Enter a topping or enter 'quit' to continue: ")
    if topping == 'quit':
        print("Done. Enjoy your pizza!")
        break;
    else:
        print(f"{topping.title()} added to your pizza.")