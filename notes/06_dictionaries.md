Chapter 6 notes

@jmerort

Oct 2025
___

# 6 - Dictionaries
A Python dictionary is a collection of key-value pairs used to store linked information pieces. A key-value pair is a value associated with another value (both keys and values can be any Python objects: variables, raw values numeric, string, boolean, lists, other dictionaries etc.). They are **defined by name-value pairs joined by `:` all enclosed in `{}` and separated by `,`**.
```
alien_0 = {'name' : 'Deoxys', 'age' : 10, 'color' : red'}
```
To **access values** of a dictionary, use the dictionary's name with the key's name in square brackets:
```
>>> alien_0['color']
red
```
Dictionaries can also be printed to see all their keys.

You can **add new values to a dictionary** like this:
```
alien_0['form'] = 'defense'
```
You can start by defining a new dictionary and add new values as you go along, same as with lists. 
```
alien_1 = {}
```

**Changing a key's value** is similar to adding a new key:
```
alien_0['type'] = 'defense'
```

One should be careful to always write the `''` signs between keys' names that are string literals. Don't write `alien_0[type]`, for instance.

You can use a `del` statement to (permamently) **remove a key-value pair** fron a dictionary:
```
del alien['age']
```

If you try to access the value of a non-existant key, you will get an error. The `get()` method of dictionaries allows for a value to be returned when the selected key does not exist. It can return a `None` type value or a value we select using the second argument.
```
>>> alien_0['height']
Traceback (most recent call last):
File "alien_no_points.py", line 2, in <module>
print(alien_0['points'])
~~~~~~~^^^^^^^^^^
KeyError: 'height'

>>> alien_0.get('height', 'The key "height" is missing.')
The key "height" is missing.
```

Because they can store lots of information, Python privdes many ways to **loop through dictionaries**, depending on if we want to check the key-value pairs, the keys or the values. To loop through the key-value pairs we can use:
```
for (key, value) in alien_0.items():
	print(f"{key} -> {value}\n")
```

The `.item()` method returns something like a list whose elements are the key-value pairs (it can't be directly subscripted like a list, though).

The `.keys()` method of dictionaries can return something like a list of all the keys in a dictionary. We can use it to loop through them:
```
for key in alien_0.keys():
	print(key)
```

In fact, looping through a dictionary does this by default. If we had written:
```
for key in alien_0:
	print(key)
```

We would have also looped through the keys, by default. Using `.keys()` might make the code easier to read, though.

The `sorted()` function can be used to return a copy of all the keys in order.
```
for key in sorted(dict.keys()):
	print(key)
```

You can **loop through** the values of a dictionary using the `.values()` method in exactly the same way. This method, however, may contain repeated values, if multiple keys have the same value. In some cases, this is not wanted. You can then use the `set()` method, that returns a **set** of the keys, which will not include any repeated element. 

You can also build a set directly like you do a list, but with curly braces instead of brackets:
```
set = {1, 2, 3, 4, 5}
```
## Nesting
To store data in even more sophisticated ways, you can nest dictionaries inside other structures or even other dictionaries.

You can use a **list of dictionaries** to store information structures about multiple objects. It's not compulsory, but this is best done when the dictionaries to be stored in the list all have the same structure, e.g. all the data of many users of a website. 

```
alien_0 = {}
alien_1 = {}

aliens = [alien_0, alien_1]
```

Lists can also be dictionary values (remember that keys and values can be any Python objects).

```
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
```

One should be careful not to nest too deeply. Programs should be as simple as feasible.

You can also **nest dictionaries inside other dictionaries**, which, though it can get very complicated, might be useful in some cases. 
