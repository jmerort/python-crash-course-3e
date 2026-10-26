# 3-8
# Seeing the World: Think of at least five places in the world you’d like
# to visit.
# •Store the locations in a list. Make sure the list is not in alphabetical order.
# •Print your list in its original order. Don’t worry about printing the list neatly;
#  just print it as a raw Python list.
# •Use sorted() to print your list in alphabetical order without modifying the
#  actual list.
# •Show that your list is still in its original order by printing it.
# •Use sorted() to print your list in reverse-alphabetical order without chang-
#  ing the order of the original list.
# •Show that your list is still in its original order by printing it again.
# •Use reverse() to change the order of your list. Print the list to show that its
#  order has changed.
# •Use reverse() to change the order of your list again. Print the list to show
#  it’s back to its original order.
# •Use sort() to change your list so it’s stored in alphabetical order. Print the
#  list to show that its order has been changed.
# •Use sort() to change your list so it’s stored in reverse-alphabetical order.
#  Print the list to show that its order has changed.
#
# Feb 2025
# @jmerort


places = ["Greece", "Egypt", "U.S.A.", "China", "Vatican", "Russia"]

print(f"Places I want to visit: {places}")

print(f"In alphabetical order: {sorted(places)}")
print(f"Places I want to visit (again): {places}")

print(f"In reverse alphabetical order: {sorted(places, reverse=True)}")
print(f"Places I want to visit (again): {places}")

places.reverse()
print(f"In reverse order: {places}")

places.reverse()
print(f"In normal order: {places}")

places.sort()
print(f"In alphabetical order: {places}")

places.sort(reverse=True)
print(f"In reverse alphabetical order: {places}")