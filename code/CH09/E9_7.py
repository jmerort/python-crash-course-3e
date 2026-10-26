"""
9-7
Admin: An administrator is a special kind of user Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171) Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on
Write a method called show_privileges() that lists the administrator’s set of
privileges Create an instance of Admin, and call your method.

Aug 2026
@jmerort
"""

from E9_5 import User

class Admin(User):
    def __init__(self, first_name, last_name, age, job, privileges=[]):
        super().__init__(first_name, last_name, age, job)
        self.privileges = ["can read post"]
        for privilege in privileges:
            self.privileges.append(privilege)

    def show_privileges(self):
        print(f"Privileges of {self.first_name.title()} {self.last_name.title()}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


if __name__=="__main__":
    regular_admin = Admin("regular", "Henchman", 20, "goon", ["can make post", "can read hidden post"])
    the_admin = Admin("Neo", "cortex", 100, "villain", ["can make post", "can make hidden post", "can delete post", "can ban user"])

    regular_admin.show_privileges()
    the_admin.show_privileges()
