# 3-10 
# Every Function: Think of things you could store in a list. For example, you
# could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items and
# then uses each function introduced in this chapter at least once.
#
# Feb 2025
# @jmerort


cities = ["Madrid", "Zamora", "Palencia", "Vigo", "Valladolid"]

print(cities)

cities.append("Ávila")
print(cities)

cities.insert(0, "Barcelona")
print(cities)

del cities[5]
print(cities)

cities.pop()
print(cities)

