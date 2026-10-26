"""
E10_11_read.py

Reader program for excercise 10_11

Oct 2026
@jmerort
"""
import json

if __name__=="__main__":
    filename = "favourite_number.txt"

    with open(filename) as file:
        favourite_number = json.load(file)

    print(f"I know your favourite number. It's {favourite_number}!")
