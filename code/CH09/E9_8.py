"""
9-8
Privileges: Write a separate Privileges class The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7
Move the show_privileges() method to this class Make a Privileges instance
as an attribute in the Admin class Create a new instance of Admin and use your
method to show its privileges.

Aug 2026
@jmerort
"""

from E9_5 import User
 
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


if __name__ == "__main__":
    my_admin = Admin("the", "boss", "40", "boss", ["can make post", "can delete user", "can read statistics"])
    my_admin.privileges.show_privileges()
