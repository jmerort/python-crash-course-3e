"""
8-10
Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it's printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.

@jmerort
Oct 2025
"""

def show_messages(messages):
    sent_messages = []
    print("--LIST OF MESSAGES--")
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

    return sent_messages

messages = [
    "Hellooo, what\'s up?",
    "WHERE IS THE MONEY????!?!?!?!?!?",
    "The name Python actually comes from the comedy show, not the animal."
    ]
sent_messages = show_messages(messages)

print(f"Proof that all messages have been moved:\nOriginal list: {messages}\nSent message list: {sent_messages}")