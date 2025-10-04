Chapter 8 notes

@jmerort

Oct 2025
___

# 8 - Functions
## 8.1 - Defining a function
**Functions** are named blocks of code that perform a particular task. They can be called independently at any point of a program, instead of having to write the same block of code many times. They can also be stored in other files, which can be imported into other programs.

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
You can passmany arguments to a function in a variety of ways: positional argument, keywords, lists, dictionaries...

When you call a function and give it a series of values, the function matches those with its arguments based on their order. E.g. if you call `function(a, b)`, `a` is assigned to the first argument of `function()` and `b` to the second. Values matchen in this way are called **positional arguments**. The order of arguments matters when they are passed in this way.

A **keyword argument** is a name-value pair that you pass to a function when you call it (instead of just passing values). E.g.:
```
describe_book(title="the oddyssey", genre="epic poetry") # Both calls are equivalent
describe_book(genre="epic poetry, title="the oddyssey") 
```
This makes function calls clearer, as you know what each argument does instead of having to check the function definition, and allows you to give the arguments in no particular order.

You can give **default values** to function parameters. If no values are given for their arguments in the function calls, the default values will be used. Thus, some function arguments can be optional. All parameters with default values must appear after the ones without them in the function definition, to allow the positional argument syntax to work (when a function is called using only the necessary arguments).
```
def describe_movie(title, genre='unknown'):
    print(f"I just saw the movie {title}.\nIt's genre is {genre}.)

describe_movie("Vertigo", "Thriller")
describe_movie("Muholland Drive")
```


