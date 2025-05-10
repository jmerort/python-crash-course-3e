"""
6-4
Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary's keys and values. When
you're sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.

May 2025
@jmerort
"""

glossary = {
  'interpreter' : 'program that reads a python script line by line and executes its instructions',
  'list' : 'ordered set of python items',
  'tuple' : 'list of items that cannot change',
  'method' : 'action Python can perform on a piece of data',
  'dictionary' : 'collection of key and value pairs used to store related information pieces', 
  'int' : 'numeric variable that holds an integer e.g. "3"',
  'string' : 'variable that holds a sequence of alphanumeric characters e.g. "Hello3"',
  'function' : 'group of statements to be executed as a block',
  'library' : 'collection of related functions and objects that can be imported and used in other programs',
  'script' : 'set of Python statements stored on a .py file',
}

print("Here are 5 definitions of Python terms:")

for term in glossary.keys():
    print(f"{term} -> {glossary[term]}")