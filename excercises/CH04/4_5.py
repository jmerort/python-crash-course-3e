# 4-5
# Summing a Million: Make a list of the numbers from one to one million, and
# then use min() and max() to make sure your list actually starts at one and ends
# at one million. Also, use the sum() function to see how quickly Python can add
# a million numbers.
# 
# Feb 2025
# @jmerort

a_milli = list(range(1, 1_000_001))

print(f"Min: {min(a_milli)}\nMax: {max(a_milli)}\nSum: {sum(a_milli)}\n")