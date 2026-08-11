"""
USER MODULE

Module for the user class of excercise 12
"""

class User():
    def __init__(self, first_name, last_name, age="unknown", job="unknown"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.login_attempts = 0

    def describe_user(self):
        print(f"The selected user is called {self.first_name.title()} {self.last_name.title()}. Their age is {self.age} and their job is {self.job}. They haved logged in {self.login_attempts} times.")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()}, good to see you! ^_^")

    def increment_login_attempts(self, n):
        if n < 1:
            print("ERROR: increment must be positive.")
        else:
            self.login_attempts += n

    def reset_login_attempts(self):
        self.login_attempts = 0


