"""
10-9
Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.

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
            pass
        else:
            print(f"Names in {file_name}:")
            for line in lines:
                print(f"- {line.rstrip('\n')}")


