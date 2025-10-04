"""
8-2
Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.

Jun 2025
@jmerort
"""

def favorite_book(title):
    """
    Prints the person's favorite book
    """
    print(f"My favorite book is {title.title()}, have you read it?")

favorite_book("the illiad")
favorite_book("la galatea")
