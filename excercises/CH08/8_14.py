"""
8-14
Cars: Write a function that stores information about a car in a diction-
ary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the func-
tion with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that's returned to make sure all the information was
stored correctly.

@jmerort
Oct 2025
"""

def build_car(manufacturer, model, **features):
    car = features
    car['manufacturer'] = manufacturer
    car['model'] = model
    return features

car = build_car('Honda', 'Civic', year=2001, owner='Yoda', status='confiscated')
print("Car parameters:")
for key in car.keys():
    print(f"{key} - {car[key]}")
