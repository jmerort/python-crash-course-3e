# 4-13
# Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# •Use a for loop to print each food the restaurant offers.
# •Try to modify one of the items, and make sure that Python rejects the
#  change.
# •The restaurant changes its menu, replacing two of the items with different
#  foods. Add a line that rewrites the tuple, and then use a for loop to print
#  each of the items on the revised menu.
#
# Feb 2025
# @jmerort

basic_foods = ("ham", "salad", "chicken", "pasta", "fish")

print("The basic food types of the buffet are:")
for food in basic_foods:
    print(food)

# basic_foods[2] = "beans" 
#TypeError: 'tuple' object does not support item assignment

# we redefine the tuple variable, which is allowed
basic_foods = ("ham", "beans", "rabbit", "pasta", "fish") 

print("The new basic food types of the buffet are:")
for food in basic_foods:
    print(food)