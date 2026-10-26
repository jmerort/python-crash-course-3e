"""
10-3
Guest: Write a program that prompts the user for their name When they
respond, write their name to a file called guest.txt.

Aug 2026
@jmerort
"""

if __name__=="__main__":
    filename = "guest.txt"

    name = input("Enter your name: ")
    with open(filename, 'w') as file:
        file.write("GuestName: ")
        file.write(name.title())
    print("Guest file succesfully created!")
