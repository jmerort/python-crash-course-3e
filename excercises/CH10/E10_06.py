"""
10-6
Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers When you try to convert
the input to an int, you’ll get a TypeError Write a program that prompts for
two numbers Add them together and print the result Catch the TypeError if
either input value is not a number, and print a friendly error message Test your
program by entering two numbers and then by entering some text instead of a
number

Aug 2026
@jmerort

I'm getting ValueError instead of TypeError, using Python version 3.14.6
"""

if __name__ == "__main__":
    print("This program sums 2 numbers.")

    a = input("Enter the first number: ")
    try: 
        a_n = int(a)
    except ValueError:
        print("Sorry, that's not an integer number, try running the program again.")
    else:       # If the first string is convertible to an int
        b = input("Enter the second number: ")
        try:
            b_n = int(b)
        except ValueError:
            print("Sorry, that's not an integer number, try running the program again.")
        else:   # If the second string is also convertible to an int
            print(f"The sum of {a_n} and {b_n} is {a_n + b_n}.")
