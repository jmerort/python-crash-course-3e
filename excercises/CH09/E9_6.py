"""
9-6
Ice Cream Stand: An ice cream stand is a specific kind of restaurant Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) Either version of
the class will work; just pick the one you like better Add an attribute called
flavors that stores a list of ice cream flavors Write a method that displays
these flavors Create an instance of IceCreamStand, and call this method

Aug 2026
@jmerort
"""

from E9_4 import Restaurant # You can just paste the Restaurant class here, if you prefer.

class IceCreamStand(Restaurant):
    def __init__(self, name):
        super().__init__(name, "ice cream")
        self.flavours = ["vanilla", "strawberry", "chocolate", "white chocolate"]
        self.toppings = ["stracciatella", "fruits", "cream"]
    
    def display_flavours(self):
        print("Here's our list of flavours:")
        for flavour in self.flavours:
            print(f"- {flavour.title()}")

    def display_toppings(self):
        print("Here's our list of toppings:")
        for topping in self.toppings:
            print(f"- {topping.title()}")

    def make_icecream(self, flavour, topping = ""):
        if topping:
            print(f"Enjoy your {flavour} ice cream with {topping} topping!")

        else:
            print(f"Enjoy your {flavour} ice cream!")


if __name__ == "__main__":
    my_parlor = IceCreamStand("polar")
    
    my_parlor.describe_restaurant()
    my_parlor.display_flavours()
    my_parlor.display_toppings()
    my_parlor.make_icecream("vanilla")
    my_parlor.make_icecream("chocolate", "cream")
