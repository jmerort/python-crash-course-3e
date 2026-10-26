"""
8-6
City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values
that are returned.

@jmerort
Oct 2025
"""

def city_country(name, country):
    return(f"{name.title()}, {country.title()}")V

print(f"I live in {city_country("valladolid", "SPAIN")}.")
print(f"I'd like to visit {city_country("athens", "greece")} some day.")
print(f"{city_country("Tokyo", "japan")} is the most populated city in the world.")