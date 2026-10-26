"""
10-4
Guest Book: Write a while loop that prompts users for their name When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt Make sure each entry appears on a
new line in the file.

Aug 2026
@jmerort
"""

if __name__=="__main__":
    filename = "guest_book.txt"

    print("Enter each guest name and press Q to exit the program:\n")
    with open(filename, 'w') as file:
        name = input("Guest name: ")
        while(name.upper() != 'Q'):
            file.write("- ")
            file.write(name)
            file.write("\n")
            name = input("Guest name: ")
    print("Guest list succesfully created!")
