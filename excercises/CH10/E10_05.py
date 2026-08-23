"""
10-5
Programming Poll: Write a while loop that asks people why they like
programming Each time someone enters a reason, add their reason to a file
that stores all the responses.

Aug 2026
@jmerort
"""

if __name__=="__main__":
    filename = "poll_answers.txt"

    print("Please tell us some reasons why you like programing! Press ENTER after each reason and Q to exit.")
    with open(filename, 'w') as file:
        reason = input("Reason: ")
        while(reason.title() != 'Q'):
            file.write("- ")
            file.write(reason)
            file.write("\n")

            reason = input("Reason: ")

    print("Poll file succesfully created!")

