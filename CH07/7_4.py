"""
7-4
Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you'll add that topping to their pizza.

May 2025
@jmerort
"""

topping = ''

while True:
    topping = input("Enter a topping or enter 'quit' to continue: ")
    if topping == 'quit':
        print("Done. Enjoy your pizza!")
        break
    else:
        print(f"{topping.title()} added to your pizza.")
    