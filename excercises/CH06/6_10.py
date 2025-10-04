"""
6-10
Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person's
name along with their favorite numbers.

May 2025
@jmerort
"""

favorite_numbers = {
    'pablo' : [3, 10],
    'javier' : [4, 24],
    'carlos' : [1,],
    'alba': [8, 9, 10],
    'antonio' : [13, 6],
}

for persona in favorite_numbers.keys():
    print (f"Los números favoritos de {persona.title()} son")
    for n in favorite_numbers[persona]:
        print(f"\t{n}")