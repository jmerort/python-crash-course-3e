"""
9-11
Imported Admin: Start with your work from Exercise 9-8 (page 178)
Store the classes User, Privileges, and Admin in one module Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.

Aug 2026
@jmerort
"""

from userbase import Admin


if __name__=="__main__":
    my_admin = Admin("Mod", "forum", 100, "moderator", ["can ban user", "can unban user"])
    my_admin.describe_user()
    my_admin.privileges.show_privileges()
