# 5-2
# More Conditional Tests: You don’t have to limit the number of tests you cre-
# ate to 10. If you want to try more comparisons, write more tests and add them
# to conditional_tests.py. Have at least one True and one False result for each of
# the following:
# •Tests for equality and inequality with strings
# •Tests using the lower() method
# •Numerical tests involving equality and inequality, greater than and less
#  than, greater than or equal to, and less than or equal to
# •Tests using the and keyword and the or keyword
# •Test whether an item is in a list
# •Test whether an item is not in a list
#
# Mar 2025
# @jmerort
#
# I had already done some of these in the previous excercise, so I'll just add some
# of the new ones here.

city = 'Zamora'
year = 2025

print("Is city equal to zamora (case insensitive)? I think it is.")
print(city.lower() == 'zamora')

print("Is the year greater than 2013? I think so.")
print(year > 2013)

print("Is the year between 2010 and 2020? I don't think so.")
print(year > 2010 and year < 2020)