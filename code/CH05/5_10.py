# 5-10
# Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
#   two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
#   been used. If it has, print a message that the person will need to enter a
#   new username. If a username has not been used, print a message saying
#   that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
#   'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
#   current_users containing the lowercase versions of all existing users.)
#
# Mar 2025
# @jmerort

current_users = ["troncoso", "xx_lonewolf_xx", "JohnSmith", "gOOnlord", "admin", "Willow"]
new_users = ["Johnsmith", "Oddyseus", "pneumatiC", "willow", "ShapeShifteR"]

#first create a lowercase version of the current user list
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

# check if the username is already in the list (case insensitive)
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Username: {user} already taken.")
    else:
        print(f"Username: {user} is available.")