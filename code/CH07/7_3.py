"""
7-3
Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.

May 2025
@jmerort
"""

n = int(input("Enter an integer number: "))

if n % 10 == 0:
    print (f"{n} is a multiple of 10.")
else:
    print (f"{n} is not a multiple of 10.")