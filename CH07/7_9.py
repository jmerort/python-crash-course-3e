"""
7-9
No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.

May 2025
"""

sandwich_orders = [
    'tuna', 'ham', 'pastrami', 'grilled_cheese', 'salad', 'pastrami', 'pastrami', 
    'tomato', 'pastrami', 'jelly', 'peanut_butter', 'banana']
finished_sandwiches = []

print(
    "ANNOUNCEMENT: As the deli has ran out of pastrami, we are sorry to announce no"
    "pastrami sandwiches will be made today.\n"
)

# Remove pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Make orders
while sandwich_orders:
    sandw = sandwich_orders.pop()
    print(f"Making a {sandw} sandwich...")
    finished_sandwiches.append(sandw)

# Print orders make
print("\nList of sandwiches made:")
for sandw in finished_sandwiches:
    print(f"\t{sandw.title()}")
