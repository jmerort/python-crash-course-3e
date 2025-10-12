Chapter 8 notes

@jmerort

Oct 2025
___

# 8 - Functions
## 8.1 - Defining a function
**Functions** are named blocks of code that perform a particular task. They can be called independently at any point of a program, instead of having to write the same block of code many times. They can also be stored in other files, which can be imported into other programs. When we need to perform the same action multiple times, even if with some variations, we ought to use functions.

```
def greet_user():             # Function definition
	"""                       # Function body
	Display a greeting
	"""
	print("HELLO!")

greet_user()                  # Function call
```

A function has 3 parts:
- Definition: Specifies the name of the function and the arguments it takes (in this case none).
- Body: Indented lines following the definition. It defines what the function does (in this case, just print "HELLO!"). If the function is to return a value, it ends with a return statement.
- Call: The function call executes the statements in the body.

If you do add arguments to the function definition, you can pass information to it, so that the function can perform its task differently depending on the inputs it's given.

```
def greet_user(name):
	"""
	Display a named greeting
	"""
	print(f"HELLO, {name.upper()}")

greet_user("Erra")
greet_user("Adapa")
```

The (generic) values specified on a function definition are its **parameters**, while the (specific) values passed to a function in its call are called **arguments**. People often mistake these meanings. 


## 8.2 - Passing arguments
You can pass many arguments to a function in a variety of ways: positional argument, keywords, lists, dictionaries...

When you call a function and give it a series of values, the function matches those with its arguments based on their order. E.g. if you call `function(a, b)`, `a` is assigned to the first argument of `function()` and `b` to the second. Values matchen in this way are called **positional arguments**. The order of arguments matters when they are passed in this way.

A **keyword argument** is a name-value pair that you pass to a function when you call it (instead of just passing values). E.g.:
```
describe_book(title="the oddyssey", genre="epic poetry") # Both calls are equivalent
describe_book(genre="epic poetry, title="the oddyssey") 
```
This makes function calls clearer, as you know what each argument does instead of having to check the function definition, and allows you to give the arguments in no particular order.

You can give **default values** to function parameters. If no values are given for their arguments in the function calls, the default values will be used. Thus, some function arguments can be optional. All parameters with default values must appear after the ones without them in the function definition, to allow the positional argument syntax to work (when a function is called using only the necessary arguments).
```
def describe_movie(title, genre=None):
    print(f"I just saw the movie {title}.")
	if genre: # If the optional argument genre has been given
	    print(It's genre is {genre}.)

describe_movie("Vertigo", "Thriller")
describe_movie("Muholland Drive")
```


## 8.3 - Return values
Most functions are used to process some data and return a value or a set of values, called **return values**. The `return` statement of a function is followed by a local value that is sent to the line that called the function. For example:
```
def sum(a, b):
	return a + b # send a + b to the caller

sum(1, 1) # receive 1 + 1 from the called function
```

Funcions can return any kind of data, including more complex structures like lists and dictionaries.
```
def build_person(first_name, last_name):
    """
	Return a dictionary of information about a person.
	"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
```

## 8.4 - Passing a list
Functions can modify the lists that are passed to them. If you don't want a function to modify a list (globally), you can use slice notation to pass a copy of that list:
```
print_models(unprinted_designs[:], completed_models) # Pass a copy of the whole unprinted_designs list
```
If you don't specifically need this, however, it's more efficient to just pass the actual list. This avoids the computational cost of creating the copy, particularly on large lists.

## 8.5 - Passing an arbitrary number of arguments
Python allows you to define functions that can accept an arbitrary number of arguments, using this notation:
```
def print_toppings(*toppings):
	print("Selected toppings:)
	for topping in toppings:
		print(f"- topping")
```
The `*` prefix tells Python to create a tuple (see [Tuples](/notes/04_working_with_lists.md#44---tuples)) with the name `toppings` and whose content is however many arguments are given to the function when it's called.

If a function has many parameters, the parameter that can accept an arbitrary number of arguments must be placed after any positional arguments. Keyword arguments may be placed after them, though.

Any function can only have one arbitrary parameter.

There is a more sophisticated use of the arbirary argument, used when you don't know what kind of information the user will be passing to the function. It uses the `**` prefix to **accept arbitrary keyword arguments**:
```
	def build_profile(first, last, **user_info):
		"""Build a dictionary containing everything we know about a user."""
		user_info['first_name'] = first
		user_info['last_name'] = last
		return user_info

	user_profile = build_profile('albert', 'einstein',
								location='princeton',
								field='physics')
	print(user_profile)
```
The double-asterisk tells the function to create a dictionary called `user-info` whose keys and values are the name-value pairs given to the function as keyword arguments, in this case: `location : princeton` and `field : physics`. This notation expects keyword arguments, so you can't give `user_info` any arguments with no names.

As you begin to write Python programs, you will start by using the most common argument types and, as you progress, eventually move on to using the most efficient each time, but it's helpful to at least be aware of the different types, as you may see them in other people's code.

## 8.6 - Storing your functions in modules
You can use functions in other Python programs by storing them in files called **modules** and then importing them. This allows you to reuse functions in other programs, and also to hide the implementation details of your functions from other programmers, which can then just import your functions and use them by importing and then calling them, without having to worry about how they work.

A module is a `.py` file that contains the code (functions, variables, classes) we want to import into other programs. 

To **import an entire module** you use an `import` statement:
```
import pizza
```
Then, you can use any function (or element) from the `pizza.py` file by using the name of the module, followed by the name of the function, separated by a dot:
```
pizza.make_pizza("pepperoni")
```
To **import a specific function from a module** use the syntax:
```
from module_name import function_name
```
When importing in this way, you don't need to use the dot notation. You can import more than one function, separating them by commas.

You can use the keyword `as` to import modules and functions using **aliases**. This helps prevent name clashes and also improve readability, by making names shorter. Aliases are typically short nicknames such as np (numpy), plt (matplotlib.pyplot), or pd (pandas).

Lastly, Python has a way of importing every function in a module using the `*` notation:
`from module_name import *`
This imports every function in the given module and lets you use them without the dot notation. However, this method is not recommended, as the module may contain functions you don't know and whose names might unexpectedly clash with yours. Thus, you should only import entire modules or specific functions from them.

All imports should be placed at the beginning of a file (except for any comments being placed at the top).

## 8.7 - Styling functions
Function (as well as module) names should be descriptive and composed of lowercase letters and underscores. The first line after the function declaration should be a comment in the docstring format (see below) that can tell a user what the function does, which inputs it expects and which outputs it produces, if any, so that a user may use your function relying only on the name and docstring. If you use any keyword arguments in the function definition or call, there should be no spaces at both sides of the equal sign.

```
def make_pizza(toppings, size='M')
	"""
	Prints the ingredients of a Pizza, consisting of a list of toppings and a size, that can be 'S', 'M' or 'L'.

	Inputs:
	- toppings : List of string toppings
	- size : 'S', 'M', or 'L' char
	"""
```