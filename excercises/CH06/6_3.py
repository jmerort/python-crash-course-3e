"""
6-3
Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let's call it a glossary.
• Think of five programming words you've learned about in the previous
  chapters. Use these words as the keys in your glossary, and store their
  meanings as values.
• Print each word and its meaning as neatly formatted output. You might
  print the word followed by a colon and then its meaning, or print the word
  on one line and then print its meaning indented on a second line. Use the
  newline character ( \n) to insert a blank line between each word-meaning
  pair in your output.

May 2025
@jmerort
"""


glossary = {
  'interpreter' : 'program that reads a python script line by line and executes its instructions',
  'list' : 'ordered set of python items',
  'tuple' : 'list of items that cannot change',
  'method' : 'action Python can perform on a piece of data',
  'dictionary' : 'collection of key and value pairs used to store related information pieces', 
}

print(
  "Here are 5 definitions of Python terms:\n"
  f"Interpreter -> {glossary['interpreter']}\n"
  f"List -> {glossary['list']}\n"
  f"Tuple -> {glossary['tuple']}\n"
  f"Method -> {glossary['method']}\n"
  f"Dictionary -> {glossary['dictionary']}\n"
  )