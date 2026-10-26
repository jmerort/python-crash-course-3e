"""
8-5
Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.

@jmerort
Oct 2025
"""

def describe_city(name, country="Spain"):
    """
    Prints a brief description of a city, consisting of the name and country.

    Inputs:
    - name : String containing the city's name.
    - country : String containing the city's country, by default "Spain".
    """
    print(f"{name.title()} is in {country.title()}.\n")


describe_city("Zamora")
describe_city("VALLADOLID")
describe_city("kyiv", "ukraine")
describe_city("Rome") # Wrong, missing country argument
