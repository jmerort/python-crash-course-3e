# Python Crash Course Solutions and Notes
Solutions to the 'TRY IT YOURSELF' excercises for the book "Python Crash Course" by Eric Matthes (3rd ed.) 

I will be posting here my solutions to the simple excercises that appear throughout this book, and also some notes. These are very simple programs with little to no use outside of the context of the textbook, but they might help somebody who is studying it. 

At the top of each program, I have pasted the exercise statement, whose credit belongs to the book's author. Everything else I have written and can be used in any way.

## How to run the programs in a virtual environment
To avoid problems with `pip` and package managements, I run all my programs from a virtual environment located in the root folder. This is relevant for the programs
from Chapter 11 onwards, which use external libraries. The installation of packages is detailed on the notes for Chapter 11.

To create a virtual environment folder named myenv, you must run this command:
```
python -m venv myenv 
```

After it's created, activate the environment by running one of the following commands. If you are on Linux or Mac:
```
source muenv/bin/activate
```

If you are on Windows:
```
myenv\scripts\activate
```

After activating the environment, you can run any of the programs by running: 
```
python3 [program_name.py]
```
