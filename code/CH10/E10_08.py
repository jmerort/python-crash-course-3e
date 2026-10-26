"""
10-8
Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a dif-
ferent location on your system, and make sure the code in the except block
executes properly.

Oct 2026
@jmerort
"""

if __name__=="__main__":
    file_names = ["cats.txt", "dogs.txt"]

    for file_name in file_names:
        try:
            with open(file_name) as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: file {file_name} not found.")
        else:
            print(f"Names in {file_name}:")
            for line in lines:
                print(f"- {line.rstrip('\n')}")


