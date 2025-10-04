Chapter 7 notes

@jmerort

Oct 2025
___

# 7 - User inputs and while loops
## The input() function
For a program to provide useful information to a user, it almost always needs to receive some kind of input from them. For that, Python uses the `input()` function. This funcion, once run, pauses the program and waits for the user to enter some text, which then assigns to a variable as a string. The text is a sequence of characters (with spaces included) until enter is hit.
```
text = input("Enter a text: ")
print (text)
```
The argument of `input()` is a prompt that should tell the user which data to input.

If we want numeric inputs we can convert the return value using functions like `int()`.
```
age = int(input("Enter your age: "))
age += 1
```

The **modulo operator** `%` gives us the remainder of the division of 2 ints.
```
if n % 2 == 0 print ("Even")
else print ("Odd")
```

## While loops
**While loops** serve to execute a section of code while certain binary condition is true. The condition is evaluated at the start of each loop.
```
i = 0;
while i < 10:
	print (i)
	i += 1
```

This kind of loop is used to keep a program running ultil the user decides or until certain condition is met, and are thus part of most major programs.
```
message = ''
while message != 'quit':
	message = input ('Enter a message or enter "quit": ')
	print (message)
```

For a program that sohuld run as long as a set of conditions is true, you can check all the conditions by using a **flag** variable. The flag is true as long as all the conditions are true. If any of them is false, the flag value is then set to false.

To **exit a loop** without executing any further statements, you use a **`break` statement**. This can be done in both `while` and `for` loops.
```
while True:
	message = input()
	if message == 'quit'
		break;
	else 
		print(message)
```

To **return to the beginning** of a loop, use a `continue` statement.
```
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
		
	print(current_number)
```

As while loops can run indefinitely, it is important to make sure that our program can actually change the condition and make it false. Otherwise, we would create an infinite loop that we can't exit. If you accidentally do that, press `Ctrl-c` to exit the program or just close the terminal window.

## Using while loops with lists and dictionaries
To modify a list or a dictionary, it's better to use `while` loops, because Python will have trouble keeping tracks of the items in `for` loops.

You can **move all elements from one list to another** using a while loop.
```
old_list = [user1, user2, etc.]
new_list = []

while old_list: # while old list is not empty
	user = old_list.pop() # remove and return the last user in old list
	new_list.append(user)
```

To remove all instances of a specific value from a list, while loops can be used, as the `remove()` method only removes the first instance of a given value.
```
while red_alien in aliens: # while there are still red aliens in the list
	aliens.remove(red_alien) # remove the first red alien
```

While loops can be used to **fill a dictionary with user input**. To do that, you prompt the user for information at each iteration of the loop, but you have to specify an input that the user can enter in order to exit.
