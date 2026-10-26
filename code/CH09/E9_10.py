"""
9-10
Imported Restaurant: Using your latest Restaurant class, store it in a mod-
ule Make a separate file that imports Restaurant Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is work-
ing properly.

Aug 2026
@jmerort
"""

from restaurant import Restaurant


if __name__=="__main__":
    my_restaurant = Restaurant("Zhangs", "chinese")
    my_restaurant.increment_number_served(12)
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
