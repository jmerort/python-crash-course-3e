Chapter 4 notes

@jmerort

Oct 2025
___

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