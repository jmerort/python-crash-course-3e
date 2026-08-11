"""
9-13
OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.


Aug 2026
@jmerort

Not sure what the difference is supposed to be here.
"""

from collections import OrderedDict


if __name__=="__main__":
    glossary = {}
    glossary['interpreter'] = 'program that reads a python script line by line and executes its instructions'
    glossary['list'] = 'ordered set of python items'
    glossary['tuple'] = 'list of items that cannot change'
    glossary['method'] = 'action Python can perform on a piece of data'
    glossary['dictionary'] = 'collection of key and value pairs used to store related information pieces'
    glossary['int'] = 'numeric variable that holds an integer e.g. "3"'
    glossary['string'] = 'variable that holds a sequence of alphanumeric characters e.g. "Hello3"'
    glossary['function'] = 'group of statements to be executed as a block'
    glossary['library'] = 'collection of related functions and objects that can be imported and used in other programs'
    glossary['script'] = 'set of Python statements stored on a .py file'

    ordered_glossary = OrderedDict()
    ordered_glossary['interpreter'] = 'program that reads a python script line by line and executes its instructions'
    ordered_glossary['list'] = 'ordered set of python items'
    ordered_glossary['tuple'] = 'list of items that cannot change'
    ordered_glossary['method'] = 'action Python can perform on a piece of data'
    ordered_glossary['dictionary'] = 'collection of key and value pairs used to store related information pieces'
    ordered_glossary['int'] = 'numeric variable that holds an integer e.g. "3"'
    ordered_glossary['string'] = 'variable that holds a sequence of alphanumeric characters e.g. "Hello3"'
    ordered_glossary['function'] = 'group of statements to be executed as a block'
    ordered_glossary['library'] = 'collection of related functions and objects that can be imported and used in other programs'
    ordered_glossary['script'] = 'set of Python statements stored on a .py file'

    print("REGULAR DICTIONARY:")
    for term in glossary.keys():
        print(f"{term} -> {glossary[term]}")

    print("ORDERED DICTIONARY:")
    for term in ordered_glossary.keys():
        print(f"{term} -> {ordered_glossary[term]}")
