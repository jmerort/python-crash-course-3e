"""
8-4
Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.

@jmerort
Oct 2025
"""

def make_shirt(size="L", message="I love Python"):
    print(f"Create a size {size} shirt with the message: {message}.\n")

make_shirt()
make_shirt(size="M")
make_shirt("M") # equivalent to the previous call
make_shirt("S", "I love C++")
make_shirt("S", message = "I love JavaScript") # Combine positional and keyword argument
# make_shirt(message = "I love C++", "M") # Wrong order, positional must go first