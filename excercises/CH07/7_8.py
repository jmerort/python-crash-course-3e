"""
7-8
Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made.

May 2025
@jmerort
"""

sandwich_orders = ['tuna', 'ham', 'grilled_cheese', 'tomato', 'jelly', 'peanut_butter', 'banana']
finished_sandwiches = []

while sandwich_orders:
    sandw = sandwich_orders.pop()
    print(f"Making a {sandw} sandwich...")
    finished_sandwiches.append(sandw)

print("\nList of sandwiches made:")
for sandw in finished_sandwiches:
    print(f"\t{sandw.title()}")
