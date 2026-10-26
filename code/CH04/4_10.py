# 4-10
# Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •Print the message The first three items in the list are:. Then use a slice to
#  print the first three items from that program’s list.
# •Print the message Three items from the middle of the list are:. Then use a
#  slice to print three items from the middle of the list.
# •Print the message The last three items in the list are:. Then use a slice to
#  print the last three items in the list.
# 
# Feb 2025
# @jmerort

animals = [
    "penguin", "duck", "goose", "ostrich",
    "owl", "crow", "eagle", "crane", "hummingbird"]

print(f"The first three animals from the list are: {animals[:3]}")
print(f"Three animals from the middle of the list are: {animals[3:6]}")
print(f"The last three animals from the list are: {animals[-3:]}\n")