"""
6-5
Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.

May 2025
@jmerort
"""


rivers = {
    'nile' : 'egypt',
    'tiber' : 'rome',
    'euphrates' : 'babylon',
    'jordan' : 'israel',
    'tajo' : 'spain',
    'rhein' : 'germany',
}

for river, location in rivers.items():
    print (f"The {river.title()} runs through {location.title()}.")

print("\nThe rivers mentioned are:")
for river in rivers.keys():
    print (river.title())

print("\nThe countries mentioned are:")
for location in rivers.values():
    print(location.title())