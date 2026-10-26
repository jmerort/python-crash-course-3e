"""
6-8
Pets: Make several dictionaries, where each dictionary represents a differ-
ent pet. In each dictionary, include the kind of animal and the owner's name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.

May 2025
@jmerort
"""

cobi = {
    'name' : 'cobi',
    'species' : 'dog',
    'owner' : 'jose',
    'size' : 'small',
    'color' : 'black',
}

mimi = {
    'name' : 'mimi',
    'species' : 'cat',
    'owner' : 'sara',
    'size' : 'medium',
    'color' : 'orange',
}

toba = {
    'name' : 'gelín',
    'species' : 'dog',
    'owner' : 'isa',
    'size' : 'big',
    'color' : 'grey',
}

pets = [cobi, mimi, toba]

for pet in pets:
    print (f"{pet['name'].title()} is a {pet['size']} {pet['color']} {pet['species']} owned by {pet['owner'].title()}.")