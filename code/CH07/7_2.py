"""
7-2
Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message say-
ing they'll have to wait for a table. Otherwise, report that their table is ready.

May 2025
@jmerort
"""

group_size = int(input("Number of dinner guests: ")) 

if group_size <= 8:
    print ("We have a table ready for you.")
else:
    print (
        f"We apologize, there are no available tables for {group_size} people yet. "
        "We're working on finding you one."
    )