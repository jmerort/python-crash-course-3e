"""
6-9
Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places for
each person. To make this exercise a bit more interesting, ask some friends to
name a few of their favorite places. Loop through the dictionary, and print each
person's name and their favorite places.

May 2025
@jmerort
"""

favorite_places = {
    'javier' : ['zamora', 'valladolid', 'mudá', 'madrid'],
    'pablo' : ['salamanca', 'rome'],
    'samuel' : ['berlin', 'madrid', 'toledo'],
}

for person in favorite_places.keys():
    print (f"{person.title()}'s favorite places are")

    for place in favorite_places[person]:
        print(f"\t{place.title()}")