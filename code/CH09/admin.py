"""
ADMIN MODULE

Module for the admin class of excercise 12
"""

from user import User


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


