"""
9-14
Dice: The module random contains functions that generate random num-
bers in a variety of ways The function randint() returns an integer in the
range you provide The following code returns a number between 1 and 6:

from random import randint
x = randint(1, 6)

Make a class Die with one attribute called sides, which has a default
value of 6 Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has Make a 6-sided die and roll
it 10 times
Make a 10-sided die and a 20-sided die Roll each die 10 times.

Aug 2026
@jmerort
"""

from random import randint 


class Die():
    def __init__(self, sides=6):
        if sides > 0:
            self.sides = sides
        else:
            print("Error: dice must have a positive number of sides.\n")
            self.sides = 1

    def roll(self):
        """Returns a random integer between 1 and the number of sides of the die"""
        print(f"Roll result: {(randint(1, self.sides))}")


if __name__=="__main__":
    regular_die = Die()
    big_die = Die(10)
    bigger_die = Die(20)

    print("Rolling the regular die...")
    for i in range (0, 10):
        regular_die.roll()

    print("Rolling the big die...")
    for i in range (0, 10):
        big_die.roll()

    print("Rolling the bigger die...")
    for i in range (0, 10):
        bigger_die.roll()


