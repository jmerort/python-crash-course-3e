# 2-7
# Stripping Names: Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().
#
# Feb 2025
# @jmerort

name = " \tJohn Smith  \n"

print(f"Name with whitespace: {name}") 
print(f"Name with no whitespace: {name.strip()}") # no wwhitespace
print(f"Name with no left whitespace: {name.lstrip()}") # no left whitespace
print(f"Name with no right whitespace: {name.rstrip()}") # no right whitespace