"""
6-6
Polling: Use the code in favorite_languages.py (page 96).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.

May 2025
@jmerort
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

poll_candidates = ['sarah', 'dean', 'ralph', 'phil', 'john', 'clyde']

for candidate in poll_candidates:
    if candidate in favorite_languages.keys():
        print (f"Thank you for taking the poll, {candidate.title()}!")
    else:
        print (f"{candidate.title()}, we invite you to take our poll :)")