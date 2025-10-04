"""
6-2
Favorite Numbers: Use a dictionary to store people's favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person's name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.

May 2025
@jmerort
"""

favorite_numbers = {
    'pablo' : 3,
    'javier' : 4,
    'carlos' : 1,
    'alba': 8,
    'antonio' : 13,
}

print((
    "Los números favoritos de cada persona son:"
    f"Pablo - {favorite_numbers['pablo']}\n"
    f"Javier - {favorite_numbers['javier']}\n"
    f"Carlos - {favorite_numbers['carlos']}\n"
    f"Alba - {favorite_numbers['alba']}\n"
    f"Antonio - {favorite_numbers['antonio']}\n"
))