# 3-6
# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# •Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
#  end of your program, informing people that you found a bigger table.
# •Use insert() to add one new guest to the beginning of your list.
# •Use insert() to add one new guest to the middle of your list.
# •Use append() to add one new guest to the end of your list.
# •Print a new set of invitation messages, one for each person in your list.
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
