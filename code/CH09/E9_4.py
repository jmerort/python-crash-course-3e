"""
9-4
Number Served: Start with your program from Exercise 9-1 (page 166)
Add an attribute called number_served with a default value of 0 Create an
instance called restaurant from this class Print the number of customers the
restaurant has served, and then change this value and print it again
Add a method called set_number_served() that lets you set the number
of customers that have been served Call this method with a new number and
print the value again
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.

Aug 2026
@jmerort
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



if __name__=="__main__":
    mi_restaurante = Restaurant(name="juanon", cuisine="castillian")

    print(f"- name = {mi_restaurante.restaurant_name}\n- cuisine = {mi_restaurante.cuisine_type}")
    mi_restaurante.describe_restaurant()

    mi_restaurante.number_served = 2 # Set attribute directly
    mi_restaurante.describe_restaurant()

    mi_restaurante.set_number_served(10) # Set attribute using method
    mi_restaurante.describe_restaurant()

    mi_restaurante.increment_number_served(-3) # Give attribute an invalid increment
    mi_restaurante.describe_restaurant() # Value didn't update
