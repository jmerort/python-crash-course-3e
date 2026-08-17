"""
10-1
Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far Start each line
with the phrase In Python you can... Save the file as learning_python.txt in the
same directory as your exercises from this chapter Write a program that reads
the file and prints what you wrote three times Print the contents once by read-
ing in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.

Aug 2026
@jmerort
"""


if __name__=="__main__":
    filename = 'learn_python.txt'

    # 1 - Printing the whole file
    with open(filename) as file:
        print(file.read().rstrip())

    # 2 - Printing the file line by line
    with open(filename) as file:
        for line in file:
            print(line.rstrip())

    # 3 - Printing the file line by line by storing it
    text = []
    with open(filename) as file:
        for line in file:
            text.append(line.rstrip())

    for line in text:
        print(line)
