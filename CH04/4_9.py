# 4-9
# Cube Comprehension: Use a list comprehension to generate a list of the first
# 10 cubes.
#
# Feb 2025
# @jmerort

# this should be same list as previous excercise
cubes = [i**3 for i in range(1, 11)]

for cube in cubes:
    print(cube)