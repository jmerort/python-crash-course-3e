# 10 - Files and Exceptions
## 10.1 - Reading from a file
Many real-world programs work with data stored in files in the computer's memory. To do it, they need to read those files file into the program's memory. This can be done by loading the whole file, or one line at a time. 

You can use the following code to **read a whole text file** and display its contents:

```python
with open('pi_digits.txt') as text:
	print(text.read()) # Print the text content
```

The `open()` function returns a **file object**. One of the methods of a file object is `read()`, which returns the text content as a string. This function adds an empty string at the end of the file, which can show up as a blank line when printed. The file needs to be opened for the object to exist. By default, Python takes the content of every file to be a string of text; to get numbers, you'll have to convert it using funcions like `int()` or `float()`.

The `with` `as` structure is not necessary to read a file, but it's used so Python automatically closes the file once it's no longer needed. If a file is not closed (which can also be done manually with a `close()` statement), the file contents can become corrupted. 

The **file path** can be either **relative**, which can be used when the file is located in the program folder or in a subfolder e.g.: `files/filename.txt`, or **absolute**, for which the full system path is specified e.g. `/home/jmerort/text_files/filename.txt`.

To **read a text file one line at a time** you can use a for loop on the file object:

```python
filepath = 'files/pi_digits.txt'

with open(filepath) as file:
	for line in file: # this adds a newline at the end of each line
		print(line)   # the print() also adds a newline
```

If we want to store the lines in a list that will remain once the file is closed, we can use the `readlines()` method:

```python
with open(filepath) as file:
	lines = file.readlines()

print(lines[1])
```

## 10.2 - Writing to a file
Storing information in files allows users to make changes that persist across multiple runs of the program. To **write strings to a text file** you must open the file in write mode. The method we saw previously:

```
open(filename, mode='w')
```

has a `mode` argument that can have one of four values:
- `'r'` : Read mode. The file won't be edited and must exist. If you don't use the argument, this is the default mode.
- `'w'` : Write mode. If no file by that name exists, it will be created. *Careful, if the file exists, it will be erased if you open it in this mode*.
- `'a'` : Append mode. The written content will go to the end of the file, without overwriting its content.
- `'r+'` : Read and write mode.

You can write using the `write()` method as follows:

```
with open(filename, 'w') as file
	file.write("I love programming!")
```

This method doesn't add any newlines. It's important to open the file in append mode, so as not to overwrite its content.

## 10.3 - Exceptions
When Python encounters code that it can't run, it creates an **exception object**. If the exception object isn't handled by the program, it crashes and the terminal prints a **traceback error** such as the following. The traceback error tells us the type of the error, in this case a `ZeroDivisionError` Knowing the type name will help us catch it.

```
Traceback (most recent call last):  
 File "/python-crash-course-3e/excercises/CH10/test.py", line 1, in <module>  
   i = 1/0  
       ~^~  
ZeroDivisionError: division by zero
```

This type of error handling should be avoided for multiple reasons: first, it isn't user friendly or easy to read, and it also could give malicious attackers information about our code. Lastly, many programs need to keep working even after the user enters invalid input. 

By catching the exception object and handling the error ourselves, we can give the user friendly feedback for how to use the program, and make our code deal with errors as intended.

To catch and handle errors we must use the  **try-except** structure.

```
try:
	print(1/0)
except ZeroDivisionError:
	print("You can't divide by zero!")
```

The program will execute the code block inside the `try:` and, if an error is raised, will look for an `except <type>:` with the same error type as the error raised. If found, it will run the code block inside it, and afterwards, it will continue running the rest of the program, because the error was handled. It is good practice to only put in the try block the code that is succeptible of raising errors. 

You can also add an `else:` block that will only run if the try block is run without exceptions raised. Any code that depends on the try code succeeding must go there.

```
try:
	result = a/b
except ZeroDivisionError:
	print("You can't divide by zero!")
else:
	print(result)
```

If the user doesn't need to see the error information, you can have the program **fail silently**. This can be done explicitly by using a `pass` statement, which tells the program to do nothing. Wether to report and error or not depends on the program.
```
try:
	count words(book)
except FileNotFoundError:
	pass
else:
```

## 10.4 - Storing data
For many programs, you will like to allow users to input some data, which could be preferences for a game, or visualization settings for an application. This data will be stored during the program's execution on a list or dictionary. To have it persist when the program is closed, you can store the data in files. 

A very common and easy to use format for doing this is **JSON** (which means JavaScript Object Notation). This format allows us to store data structures directly in a file and easily load them. It is used in multiple programming languages. 

We can **store an object in a json file** using the `dump()` method of the **json module**. This method takes as arguments first the object to be stored and then the file object. The json extension is used to indicate the content. 
```
import json

lista = [1, 2, 3, 4]
with open("numbers.json", 'w') as file:
	json.dump(list, file)
```

Then, in another program, we can **load a stored json object** using the `load()` method, which takes as argument the file object, and also requires the file to be opened. 
```
import json
with open("numbers.json") as file: # Read mode by default
	lista = json.load(file)
print(lista)
>>> [1, 2, 3, 4]
```

## 10.5 - Refactoring
As you create programs, you will often come to a point, where you have a program that works, but that could have a better structure. Breaking up a program into functions that do simple jobs is called **refactoring**, and produces code that's easier to use, read, and maintain.

Each function should do a specific action that can be stated with a simple verb statement. For example, if a function:
- Takes A, does X with it, outputting B : It's a good, modular function.
- Takes A, does X with it and then does Y, outputting C : It probably could be broken up into 2 functions.
