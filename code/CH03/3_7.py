# 3-7
# Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.
# •Start with your program from Exercise 3-6. Add a new line that prints a
#  message saying that you can invite only two people for dinner.
# •Use pop() to remove guests from your list one at a time until only two
#  names remain in your list. Each time you pop a name from your list, print a
#  message to that person letting them know you’re sorry you can’t invite them
#  to dinner.
# •Print a message to each of the two people still on your list, letting them
#  know they’re still invited.
# •Use del to remove the last two names from your list, so you have an empty
#  list. Print your list to make sure you actually have an empty list at the end of
#  your program.
#
# Feb 2025
# @jmerort


dinner_guests = ["Sokrates", "Jesus", "Ye", "Buddha", "Kim Jong Un"]

print("\n-INVITATIONS-")
print(f"Greetings, {dinner_guests[0]}, you are invited to the dinner, which will be held at 8:00 p.m. in the dinner hall April 21. See you there!")
print(f"Greetings, {dinner_guests[1]}, you are invited to the dinner, which will be held at 8:00 p.m. in the dinner hall April 21. See you there!")
print(f"Greetings, {dinner_guests[2]}, you are invited to the dinner, which will be held at 8:00 p.m. in the dinner hall April 21. See you there!")
print(f"Greetings, {dinner_guests[3]}, you are invited to the dinner, which will be held at 8:00 p.m. in the dinner hall April 21. See you there!")
print(f"Greetings, {dinner_guests[4]}, you are invited to the dinner, which will be held at 8:00 p.m. in the dinner hall April 21. See you there!")

print(f"\nANNOUNCEMENT\nWe're sorry to announce that {dinner_guests[0]} will not be able to attend the dinner, we will promptly look for a new dinner guest and send out new invitations.")

dinner_guests = ["Plato", "Jesus", "Ye", "Buddha", "Kim Jong Un"]

print("\n-INVITATIONS-")
print(f"Greetings, {dinner_guests[0]}, you are invited to the dinner, which will be held at 8:00 p.m. in the dinner hall April 22. See you there!")
print(f"Greetings, {dinner_guests[1]}, you are invited to the dinner, which will be held at 8:00 p.m. in the dinner hall April 22. See you there!")
print(f"Greetings, {dinner_guests[2]}, you are invited to the dinner, which will be held at 8:00 p.m. in the dinner hall April 22. See you there!")
print(f"Greetings, {dinner_guests[3]}, you are invited to the dinner, which will be held at 8:00 p.m. in the dinner hall April 22. See you there!")
print(f"Greetings, {dinner_guests[4]}, you are invited to the dinner, which will be held at 8:00 p.m. in the dinner hall April 22. See you there!")

print("\n-ANNOUNCEMENT-\nWe're happy to announce that the dinner hall just got a bigger table, so three new dinners guests will be present at the dinner. You will be informed shortly.")

dinner_guests.insert(0, "F. de Quevedo")
dinner_guests.insert(3, "Barron Trump")
dinner_guests.append("Muhammad")

print("\n-INVITATIONS-")
print(f"Greetings, {dinner_guests[0]}, you are invited to the dinner, which will be held at 8:20 p.m. in the dinner hall April 23. See you there!")
print(f"Greetings, {dinner_guests[1]}, you are invited to the dinner, which will be held at 8:20 p.m. in the dinner hall April 23. See you there!")
print(f"Greetings, {dinner_guests[2]}, you are invited to the dinner, which will be held at 8:20 p.m. in the dinner hall April 23. See you there!")
print(f"Greetings, {dinner_guests[3]}, you are invited to the dinner, which will be held at 8:20 p.m. in the dinner hall April 23. See you there!")
print(f"Greetings, {dinner_guests[4]}, you are invited to the dinner, which will be held at 8:20 p.m. in the dinner hall April 23. See you there!")
print(f"Greetings, {dinner_guests[5]}, you are invited to the dinner, which will be held at 8:20 p.m. in the dinner hall April 23. See you there!")
print(f"Greetings, {dinner_guests[6]}, you are invited to the dinner, which will be held at 8:20 p.m. in the dinner hall April 23. See you there!")
print(f"Greetings, {dinner_guests[7]}, you are invited to the dinner, which will be held at 8:20 p.m. in the dinner hall April 23. See you there!")

print("\nANNOUNCEMENT\nWe're very sorry to announce that, due to a reservation problem in the dinner hall, only two people will be able to attend. We will update you in time.")

uninvited = dinner_guests.pop()
print(f"I'm sorry, {uninvited}, but you will not be coming to the dinner.")
uninvited = dinner_guests.pop()
print(f"I'm sorry, {uninvited}, but you will not be coming to the dinner.")
uninvited = dinner_guests.pop()
print(f"I'm sorry, {uninvited}, but you will not be coming to the dinner.")
uninvited = dinner_guests.pop()
print(f"I'm sorry, {uninvited}, but you will not be coming to the dinner.")
uninvited = dinner_guests.pop()
print(f"I'm sorry, {uninvited}, but you will not be coming to the dinner.")
uninvited = dinner_guests.pop()
print(f"I'm sorry, {uninvited}, but you will not be coming to the dinner.")

print("\n-NEW INVITATIONS-")
print(f"Greetings, {dinner_guests[0]}, you are still invited to the dinner, which will be held at 8:20 p.m. in the dinner hall April 23. See you there!")
print(f"Greetings, {dinner_guests[1]}, you are still invited to the dinner, which will be held at 8:20 p.m. in the dinner hall April 23. See you there!")

del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)