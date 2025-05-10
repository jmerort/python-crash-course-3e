"""
6-11
Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city's dictionary should be something like
country, population, and fact. Print the name of each city and all of the infor-
mation you have stored about it.

May 2025
@jmerort
"""

cities = {
    'zamora' : {
        'country' : 'spain',
        'population' : 	59506,
        'fact' : 'Zamora has the most romanesque churches of any city in the world.',
    },

    'madrid' : {
        'country' : 'spain',
        'population' : 3277000,
        'fact' : 'Madrid is the only capital in Europe entirely surrounded by mountains.'
    },

    'valladolid' : {
        'country' : 'spain',
        'population' : 300618,
        'fact' : 'Christopher Columbus died in Valladolid in 1506',
    },
}

for city in cities:
    print (f"Some info about {city.title()}")
    for key, val in cities[city].items():
        print(f"{key.title()}\t->\t{val}")
    print("\n")