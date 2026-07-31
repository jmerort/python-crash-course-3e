"""
9-2
Three Restaurants: Start with your class from Exercise 9-1 Create three
different instances from the class, and call describe_restaurant() for each
instance.

Jul 2026
@jmerort
"""

from E9_1 import Restaurant # I will try here to import instead of copy the whole class def

def main():
    rest_1 = Restaurant("vitos", "italian")
    rest_2 = Restaurant("primos", "mexican")
    rest_3 = Restaurant("le grosse fromage", "french")

    rest_1.describe_restaurant()
    rest_2.describe_restaurant()
    rest_3.describe_restaurant()


main()
