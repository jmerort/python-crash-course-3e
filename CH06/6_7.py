"""
6-7
People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionar-
ies in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.

May 2025
@jmerort
"""


person_1 = {
    'name' : 'ye',
    'last_name' : 'west',
    'age' : 47,
    'city' : 'chicago'
}

person_2 = {
    'name' : 'robert',
    'last_name' : 'prevost',
    'age' : 69,
    'city' : 'rome',
}

person_3 = {
    'name' : 'ian',
    'last_name' : 'goodfellow',
    'age' : 38,
    'city' : 'stanford',
}

people = [person_1, person_2, person_3]

for person in people:
    for category, data in person.items():
        print(f"{category.title()}\t{data}")
    print("\n")