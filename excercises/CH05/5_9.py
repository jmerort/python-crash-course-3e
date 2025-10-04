# 5-9
# No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct mes-
#   sage is printed.
#
# Mar 2025
# @jmerort

users = []

if users: # check if list not empty
    for username in users:
        if username == "admin":
            print("Greetings, admin, would you like to see the latest status report?")
        else:
            print(f"Hello, {username}, welcome back to the site :-)")
else:
    print("We really need to find some users :/")