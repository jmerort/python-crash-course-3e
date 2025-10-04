Chapter 3 notes

@jmerort

Oct 2025
___


# 3 - Introducing lists
A list is an ordered collection of items. The elements of a list are indicated by square brackets:
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
To delete a particular value from a list, use `remove()`, which deletes the first instance of it:
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
