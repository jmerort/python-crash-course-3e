"""
8-9
Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.

@jmerort
Oct 2025
"""

def show_messages(messages):
    print("--LIST OF MESSAGES--")
    for message in messages:
        print(message)

messages = [
    "Hellooo, what\'s up?",
    "WHERE IS THE MONEY????!?!?!?!?!?",
    "The name Python actually comes from the comedy show, not the animal."
    ]
show_messages(messages)
