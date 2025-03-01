09-02-2025 15:26

Estado: #Niño 

Resumen: Apuntes de este libro de Python

# Notas
# 1 - Getting started
You can run lines of Python code using the interpreter from a terminal window, instead of writing and running a whole program.

To install Python, first check if it's already installed by typing `python3` if you're on Linux or Mac and `python` if you're on Windows in the command line/terminal application. If it isn't installed, or if you want a newer version, go to https://python.org and look for the downloads section, where the installer should be.

To write and run Python programs on VSCode, first install the Python extension provided by Microsoft. 

Python files have a .py extension.

To run a python file press the run symbol on VSCode or run 
```
python3 program.py
```
on the command line.

# 2 - Variables and simple data types
A **variable** is a name associated with a value (number, words etc.), which can be changed during the course of a program. (In other languages, the "named box" metaphor is helpful, but not in Python.)

Variable names in Python are series of letters (uppercase or lowercase), numbers and underscores. They can begin with a letter or underscore, not with a number. One should avoid keywords (like `print`) and function names as variable names. They should also be short, clear (avoid 1 l O 0 confusions) and descriptive.

A **string** is a series of characters inside single or double quotes
```
"This is a string"
'Th!$ is 4($0 a $7r!ng'
```
You can use quotes and apostrophes (within double quotes) within strings:
```
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```
A **method** is an action Python can perform on a piece of data. They use dot notation and are followed by parentheses. The method inputs (if any) go inside them. Some useful methods for strings are:
```
name = "ada LoveLaCe"

name.title() #returns "Ada Lovelace"
name.upper() #"ADA LOVELACE"
name.lower() #ada lovelace
```
`name.lower()` is often used to store data in a consistent way, so you don't have to deal with how the users capitalize names.

To include variables in strings we have to use f-strings or format strings, which are preceeded by an `f` and have the variable names in between brackets:
```
print(f"Hello, {name.title()}!")  #Hello, Ada Lovelace!.
```

Newlines and tabs are represented by `\n` and `\t`.

To **strip whitespace** from a string we use these methods:
```
name.rstrip() #strip whitespace from right side
name.lstrip() # '' from left side
name.strip()  # '' from both sides
```

To remove a prefix from a string we use `removeprefix()`. The prefix has to be at the beginning of the string.
```
address.removeprefix('https://')
```
There is also `removesuffix()`, which works as expected.

Python has many **number** classes, the most simple being **integers**. Integers can be added (+), substracted (-), multiplied (\*) and divided (/). Powers are representedby 2 multiplication symbols (\*\*).

Numbers with decimal points are called **floats**. When you divide any integers, you always get a float. If you mix integers and floats in any other operation, you also get a float.

To represent big numbers in a more readable way, you can put underscores, which are only asethetic:
```
n = 10_000_000
# is the same as
n = 10000000
```
Multiple assignment:
```
a, b, c = 1, 2, 3
```
A **constant** is a variable whose value stays the same throughout the life of a program. Python doesn't have a built-in constant type, so python programmers indicate constants by naming them in all caps.
```
ACCELERATION = 9.8
```

Comments are written to indicate what you code is supposed to do and how you're doing it. In Python, comments are single line and indicated by `#`.

# 3 - Introducing lists
A list is an ordered collection of items. The elements of a list area indicated by square brackets:
```
authors = ['Cervantes', 'Dante', 'Camoens']
```
Whole lists can be printed `print(authors)`.

You can access list eleemnts with index notation:
```
>>> print(authors[2])
Camoens
```
The index `[-1]` returns the last element of a list, `[-2]` the second-to-last and so on.

## Modifying, Adding, and Removing list Elements
You can change the value of any item of a list.

To add values to a list, it's most common to use `append()`, which inserts a new element at the end. This way you can define an empty list and grow it throughout the program:
```
>>> list = []
>>> list.append(1)
>>> list.append(2)
>>> print(list)
[1, 2]
```
You can insert elements in any position using `insert()`, which takes as arguments the index of the position in which to insert the value, and the value. This methods shifts existing elements to the right. 
```
>>> list.insert(1, 3)
>>> print(list)
[1, 3, 2]
```
List elements can be deleted according to their index or to their value. `del()` removes the element at the given index and doesn't return anything. 
```
>>> del list[0]
[3, 2]
```
If you want to use the element you want to remove from a list in any way, use the `pop()` method, which returns it. If you give it no index, it pops the last element.
```
>>> n = list.pop(0)
>>> print(n)
3
```
To delete a particular value from a list, use `delete()`, which deletes the first instance of it:
```
>>> list = [1, 2, 2, 3]
>>> list.remove(2)
[1, 2, 3]
```
## Organizing a list
The list method `.sort()` sorts the elements of a list alphabetically permanently, returning nothing. To sort them in reverse order use the argument `list.sort(reverse=True)`.

To get a sorted copy of a list use `sorted(list)` function, which can also accept a `reverse` argument.

The `.reverse()` list method reverses the order of the elements of a list.

To get the number of elements of a list, use the `len()` function.

Careful! The .sort(), .reverse() methods just change the order, they don't return anything.

# 4 - Working with lists
In this chapter we'll learn how to work efficiently with lists, regardless of how many elements they have, by looping through them.

## Looping through a list
To perform the same action for every element of a list, Python uses the `for` loop, which assigns to a given variable the values of every list element, one at a time. 
```
names = [Matthew, Mark, Luke, John]
for name in names:
	print(n)
```
Every indented line following the `:` is considered to be inside the loop and will be executed every iteration. In Python, therefore, **indentation** is not just aesthetic, it indicates how a group of statements is realted to the rest pf the program. It thus forces the programmer to express the program structure in a visual way. It's use is similar to curly brackets in other languages like C/C++.

## Making numerical lists
To create a list of ordered integers, you can use the `range()` function, which returns a range of integers, which can be converted into a list or used in a loop
```
>>> a = range(0,5)
>>> print(a)
range(0,5)

>>> b = list(range(0,5))
>>> print(b)
[1,2,3,4]

>>> for n in range(3):
>>> 	print(n)
0
1
2
```
Keep in mind that the last element of the range will not be used, as the range stops when it is reacher or surpassed. You can give a third argument for the step size, which is 1 by default. The begin point is 0 by default, so you can also give it just one argument.
```
>>> for n in range(0, 12, 5):
>>>	print(n)
0
5
10
```

The simple functions `min()`, `max()` and `sum()` perform simple statistical operations on lists of numbers:
```
>>> numbers = [1, 2, 3, 4]
>>> min(numbers)
1
>>> max(numbers)
4
>>> sum(numbers)
10
```

A **list comprehension** is a compact way of creating numerical lists, which uses a loop on the same line as the list definition.
```
>>> squares = [value**2 for value in range(1,11)]
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
This is a bit confusing at first, but if you remember the syntax it can be useful, and  people very often use it in their code.

## Working with part of a list
A subset of the elements of a list is called a **slice**. To make a slice, you specify the index of the first and last elements of the slice, the last one not included. 
```
>>> players = ['charles', 'martina', 'michael', 'florence', 'eli']
>>> print(players[0:3])
['charles', 'martina', 'michael']
```
If you ommit an index of the slice, the slice starts at the beginning or ends at the end.
```
>>> print(players[3:])
['florence', 'eli']
```
You can use negative indexes to refer tho the last elements of the list.
```
>> print(players[-3:]) # last 3 players
```
You can take slices of only the n-th elements by using a third index, which is the step size of the slice. The following line would print every second player from index 0 to 4 (in this case it would print players[0], players[2] and players[4]):
```
>>> print(players(:5:2))
```
Slices are used when you want to select particular information from a list. You could sort a numerical list and then take the n biggest or smallest values, partition a list to display it on a screen...

Slices are also used to **copy lists**. In Python, if you try to assign to a new list the name of another list, instead of assigning it its value Python links the new list to the old one, so both point to the same data in memory, instead of the new one being a copy. This isn't what happens with regular variables and can cause problems if it goes unnoticed. 
```
old_list = ['item_1', 'item_2', 'item_3']
new_list = old_list[:] #assign a copy of the entire old list
```

## Tuples
To create a list of items that cannot change, you define a **tuple**. They return error when the program tries to change the value of any of its members. (You can redefine a tuple variable, assigning it another tuple, though.)
```
dimensions = (200, 50)
dimensions[0] = 250 # this gives an error
```
In truth, the parentheses are just used for clarity, what defines a tuple is the comma, so to have a 1-element tuple you would define 
```
tup = 200,
```
or
```
tup = (200,)
```

## Styling your code
As almost any code will be read much more often that it will be written, it's always a good idea to aim for code that's easier to read, rather than easier to write. 

The PEP 8 document is the standard Python style guide. It contains the aesthetic conventions that professional Python programmers follow. 

The default indentation level is four spaces. Make sure to have the tab key insert 4 spaces instead of a tab character, as this chan confuse the interpreter. 

The PEP-8 recommended line length is less than 80 characters per line to allow readability when mutiple tabs are on-screen. (The default VSCode code window size when not full screen is a good indicator.)

Blank lines are used to group part of your program, but should not be abused. 

# 5 - If statements
Programming almost always involves checking for certain conditions and deciding which action to take based on these. 

A Python `if` statement is based on an expression that can be evaluated as either `True` or `False`. This is called the conditional test. If the conditional test evaluates to True, the (indented) code following the if statement is executed. If it evaluates to false, the code following the if is ignored and, if there is an `else:`, the code following it is executed.
```
for car in cars:
	if car == "bmw":
		print("BMW")
	else:
		print(car)
```
The equality operator `==` returns `True` if the values on each side of it are the same and `False` if they are different. (Difference between expressions and statements.)

The inequality operator `!=` does the opposite.

You can also include the order operators `<`, `>`, `<=` and `>=` in conditional statements.

The keywords `and` and `or` are used to evaluate multiple expressions. They return `True` or `False` depending on the values of the two logical expressions on each side. If both are true, `and` returns `True` and, if at least one is true, `or` returns `True`.
```
>>> age_0 = 5
>>> age_1 = 12

>>> age_0 >= 10 and age_1 >= 10 
False
>>> age_0 >= 10 or age_1 >= 10
True
```
To check if a value is in a list, you can use the keyword `in`:
```
if user in banned_users:
	print("lol banned")
	
if user not in banned_users:
	print("login succesful")
```
The `not` keyword returns the opposite value of the following logical expression.

A conditional test is also called a boolean expression. You can have boolean type variables, that can only have `True` or `False` as values and are used to track binary conditions.
```
flag = True
```


# D - Using Git for version control
To **install Git**, you can check for an installer in https://git-scm.com or run `sudo apt install git` if you're on Linux. 

To check if it's already installed run `git --version` or `git -v` in the command line.

Before doing anything with Git, you must **configure** it, by providing a username and an email address, though it can be a fake one. 
```
git config --global user.name "name"
git config --global user.email "mail@example.com"
```
To give a name (usually we use "main") to the default branch of each project use:
```
git config --global init.defaultBranch main
```

To **start a Git project**, we first create a folder in which the files whose changes we want to track will be stored. There will be some files that we don't want to track, such as those automatically generated by IDE's, compilers, the Python interpreter and so forth. To tell Git not to track them we include their names in a file falled `.gitignore`.
For example, a Python project will have an ignore file that includes:
```
__pycache__/
```
To have the automatically created files in that directory **ignored**. (On MAC one should also add a `.DS_Store`, to ignore these information files.)

Files whose names begin with dots are sometimes hidden; you can change this in the file explorer settings.

To **initialize** a Git repository, go to its folder in the command line and run
```
git init
```
This will create a new hidden directory named `.git`, where the project management files will be located. You don't need to do anything with it. 

To check the project **status** run 
```
git status
```
A branch is a version of the project. 

To **add** the current directory files to the project (those not already tracked), run
```
git add .
```
After making changes to the tracked files, we can make a **commit** and add a message with the `-m` argument. A commit is a snapshot of the project at one point in time.
```
git commit -m "Started the project!"
```
Now the status of the project should tell us we have a clean working tree. If not, we probably forgot to do something before making the commit. 

To check the **log** of all commits made to a project, use:
```
git log
```
this will print, among other info, the 40-character reference ID of each commit. It records who made the commit, when it was made, and the message recorded. To see only the most important info, use:
```
git log --pretty=oneline
```

When we **change the file further**, we will commit the changes using:
```
git commit -am "New changes"
```
The `-a` flag tells Git to add all modified files in the repo to the current commit. If you create new files and want to track them too, run `git add .` again.

To **abandon a change**, going back to the previous working state, before we have commited the "bad" version, we use:
```
git restore .
```
This restores our program to the last commited version. It can be used with specific files or with all files (if we use `.`). This allows us to make as many changes as we want to a file and, if they don't work, we just discard them automatically.

You can **revisit a commit** using the checkout command and giging it the first six characters of the reference ID (see log):
```
git checkout 32c312
```
You will then leave the main branch and enter into a **detached HEAD** state, the head being the commit you are checking out. In this state you can see the files from a previous commit and run it. For beginner Git users, it's best to not modify anything here.

To go back to the main branch, use:
```
git switch -
```
To **go back permanently to a previous commit**, first check the satus to make sure you are on main and then run `git reset` with the ID of the commit you want to go back to:
```
git reset --hard cea13d
```

Finally, to **delete the Git history** of a project, delete the `.git/` directory using
```
rm -rf .git/
```
This will not delete the current project files, but you will lose all previous commit info and the ability to go back to previous versions. After deleting the history, you can start tracking changes again by following the same steps as before.

# Referencias
PYTHON CRASH COURSE, 3RD EDITION. (2023) by Eric Matthes.