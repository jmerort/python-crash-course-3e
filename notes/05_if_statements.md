Chapter 5 notes

@jmerort

Oct 2025
___


# 5 - If statements
Programming almost always involves checking for certain conditions and deciding which action to take based on these. 

A Python **if statement** is based on an expression that can be evaluated as either `True` or `False`. This is called the conditional test. If the conditional test evaluates to True, the indented code following the if statement is executed ; if it evaluates to false, the code following the if is ignored and, if there is an `else:`, the code following it is executed.
```
for car in cars:
	if car == "bmw":
		print("BMW")
	else:
		print(car)
```
To test a condition with more than 2 possibilities, we can use more complex **if-elif-else** chains (the elif being a shorter way of writing else if, which can be used as many times we want):
```
if age > 70:
	print("You're retired")
elif age > 18:
	print("You're of age to work.")
else:
	print("You're still underage.")
```
The `else` operator is not necessary in Python.


The equality operator `==` returns `True` if the values on each side of it are the same and `False` if they are different.

The inequality operator `!=` does the opposite.

You can also include the order operators `<`, `>`, `<=` and `>=` in conditional statements.


The keywords `and` and `or` are used to evaluate multiple expressions. They return `True` or `False` depending on the values of the two logical expressions on each side. If (and only if) both are true, `and` returns `True`; if (and only if) at least one is true, `or` returns `True`.
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

We can use non boolean variables in conditional tests. Numeric variables will be considered `True` if they are not zero, while lists will be considered `True` if they are not empty. This is a way to **check if a list is empty**: 
```
stuff = []

if stuff:
	print(stuff)
else:
	the list is empty
```
