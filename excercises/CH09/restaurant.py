"""
RESTAURANT MODULE

This module contains the restaurant class and its methods.
"""

class Restaurant():
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Our restaurant is called {self.restaurant_name.title()} and specializes in {self.cuisine_type} cuisine.\nIt has served so far {self.number_served} clients.\n")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!\n")

    def set_number_served(self, n):
        if n < 0:
            print("ERROR: number of clients served can't be negative.")
        else:
            self.number_served = n
    
    def increment_number_served(self, n):
        if n < 1:
            print("ERROR: increment must be positive.")
        else:
            self.number_served += n
