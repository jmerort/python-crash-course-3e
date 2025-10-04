# 5-1
# Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# •Look closely at your results, and make sure you understand why each line
#  evaluates to True or False.
# •Create at least 10 tests. Have at least 5 tests evaluate to True and another  
#  5 tests evaluate to False.
#
# Mar 2025
# @jmerort

train = 'renfe'
trains = ['renfe', 'alvia', 'ave', 'metro']

print("Is train == 'renfe'? I predict True.") # same word
print(train == 'renfe')

print("\nIs train == 'ave'? I predict False.") # different word 
print(train == 'ave')

print("\nIs train == 'Renfe'? I predict False.") # capitalized
print(train == 'Renfe')

print("\nIs train == 'renfe '? I predict False.") # adding a whitespace
print(train == 'renfe ') 

print("\nIs train != 'ave'? I predict True.") # inequality operator
print(train != 'ave')

print("\nIs train renfe or alvia or ave? I predict True.") # or operator
print(train == 'renfe' or train == 'alvia' or train == 'ave')

print("\nIs train renfe and alvia? I predict False.") # and operator
print(train == 'renfe' and train == 'alvia')

print("\nIs train in the train list? I predict True.") # in list operator
print(train in trains)

print("\nIs train not in the train list? I predict False.") # Train is not in the list
print(train not in trains)

print("\nIs train bigger than 'ave'? I predict False.") # Order operator (strings later in alphabetical order are bigger I think)
print(train > 'ave')
