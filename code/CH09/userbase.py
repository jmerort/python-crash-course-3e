"""
USERBASE MODULE

Module that contains the classes related to user types and 
their methods.
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


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = ["can read post"]
        for privilege in privileges:
            self.privileges.append(privilege)

    def show_privileges(self): # Now this method can't use the user's name 
        print(f"Privileges of the user:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, job, privileges=[]):
        super().__init__(first_name, last_name, age, job)
        self.privileges = Privileges(privileges)


