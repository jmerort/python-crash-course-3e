"""
6.1
Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each piece
of information stored in your dictionary.

May 2025
@jmerort
"""

datos = {
    'name' : 'ye',
    'last_name' : 'west',
    'age' : 47,
    'city' : 'chicago'
}

print(f"Name - {datos.get('name').title()}\nAge - {datos.get('age')}\nCity -  {datos.get('city').title()}")
