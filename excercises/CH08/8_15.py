"""
8-15
Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.

@jmerort
Oct 2025

I'll just put the functions in a module called `printing_functions.py` and
use them here.
"""

import printing_functions as pf # import the module giving it the alias "pf"


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
pf.print_models(unprinted_designs, completed_models) # use the functions from "pf" with the dot notations
pf.show_completed_models(completed_models)
