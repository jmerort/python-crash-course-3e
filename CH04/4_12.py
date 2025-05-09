# 4-12
# More Loops: All versions of foods.py in this section have avoided using
# for loops when printing, to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.
# 
# I used the one from page 63 (3rd ed)
#
# Feb 2025
# @jemrort

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

print()