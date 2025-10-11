"""
8-12
Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that's being ordered. Call the function three times, using a different num-
ber of arguments each time.

@jmerort
Oct 2025
"""

def make_sandwich(*ingredients):
    print("Making sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich("ham", "cheese", "lettuce")
make_sandwich("bacon")
make_sandwich() # Arbitrary argument functions also accept no arguments