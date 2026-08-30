"""
10-7
Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number

Aug 2026
@jmerort
"""

if __name__ == "__main__":
    # Flags to check if valid numebrs have been entered
    a_valid = False
    b_valid = False

    print("This program sums 2 numbers.")

    while(a_valid == False):
        a = input("Enter the first number: ")
        try: 
            a_n = int(a)
        except ValueError:
            print("Sorry, that's not an integer number, try again.")
        else:
            a_valid = True

    while(b_valid == False):
        b = input("Enter the second number: ")
        try:
            b_n = int(b)
        except ValueError:
            print("Sorry, that's not an integer number, try again.")
        else:
            b_valid = True

    print(f"The sum of {a_n} and {b_n} is {a_n + b_n}.")
