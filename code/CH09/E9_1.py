"""
9-1
Restaurant: Make a class called Restaurant The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open
Make an instance called restaurant from your class Print the two attri-
butes individually, and then call both methods.

Jul 2026
@jmerort
"""

class Restaurant():
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print(f"Our restaurant is called {self.restaurant_name.title()} and specializes in {self.cuisine_type} cuisine.\n")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!\n")


if __name__=="__main__":
    mi_restaurante = Restaurant(name="juanon", cuisine="castillian")

    print(f"- name = {mi_restaurante.restaurant_name}\n- cuisine = {mi_restaurante.cuisine_type}")
    mi_restaurante.describe_restaurant()
    mi_restaurante.open_restaurant()

