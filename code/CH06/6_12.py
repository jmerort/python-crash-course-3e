"""
6-12
Extensions: We're now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example pro-
grams from this chapter, and extend it by adding new keys and values, chang-
ing the context of the program, or improving the formatting of the output.

May 2025
@jmerort

I have extended the alien.py example from page 96
"""


alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['name'] = 'neil'
alien_0['scpecies'] = 'grey'

print("ALIEN DATA")
for key, val in alien_0.items():
    print(f"{key}\t{val}")