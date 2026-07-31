"""
9-3
Users: Make a class called User Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile Make a method called describe_user() that prints a summary
of the user’s information Make another method called greet_user() that prints
a personalized greeting to the user
Create several instances representing different users, and call both methods
for each user.

Jul 2026
@jmerort
"""

class User():
    def __init__(self, first_name, last_name, age="unknown", job="unknown"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

    def describe_user(self):
        print(f"The selected user is called {self.first_name.title()} {self.last_name.title()}. Their age is {self.age} and their job is {self.job}.\n")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()}, good to see you! ^_^")

if __name__ == "__main__":
    user_1 = User("Bob", "the builder", 28, "builder")
    user_2 = User("donald", "trump", 80, "president")
    user_3 = User("kevin", "Schmo", 21, "special_agent")
    user_4 = User("johnny", "hobo")

    user_1.describe_user()
    user_2.describe_user()
    user_3.describe_user()
    user_4.describe_user()

    user_2.greet_user()
    user_4.greet_user()
