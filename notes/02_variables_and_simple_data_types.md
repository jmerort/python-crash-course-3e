Chapter 2 notes

@jmerort

Oct 2025
___

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
