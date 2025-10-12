"""
8-16
Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *

@jmerort
Oct 2025

I will use the `favorite_book()` function from excercise 8.2, which 
I stored in the `books.py` module.
"""

# 1) Module import
#import books
#books.favorite_book("Ethica More Geometrico Demonstrata")

# 2) Function import
#from books import favorite_book
#favorite_book("Ethica More Geometrico Demonstrata")

# 3) Function import with alias
#from books import favorite_book as fav
#fav("Ethica More Geometrico Demonstrata")

# 4) Import all functions from module
from books import *
favorite_book("Ethica More Geometrico Demonstrata")
