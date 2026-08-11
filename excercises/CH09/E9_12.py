"""
9-12
Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.

Aug 2026
@jmerort
"""

from admin import Admin # The admin module will itself import User


if __name__=="__main__":
    my_admin = Admin("john", "doe", 33, "moderator", ["can_ban_user", "can_make_post", "can_delete_post"])
    my_admin.describe_user()
    my_admin.privileges.show_privileges()
