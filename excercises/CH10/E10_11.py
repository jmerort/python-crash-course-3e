"""
10-11
Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____.


The reader program is called "10_11_read.py"

Oct 2026
@jmerort
"""
import json

if __name__=="__main__":
    filename = "favourite_number.txt"

    favourite_number = input("What's your favourite number?\n>>> ")

    try:
        float(favourite_number)
    except ValueError:
        print("Sorry, that's not a number.")
    else:
        with open(filename, 'w') as file:
            json.dump(favourite_number, file)
