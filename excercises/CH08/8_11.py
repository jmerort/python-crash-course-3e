"""
8-11
Archived Messages: Start with your work from Exercise 8-10. Call the func-
tion send_messages() with a copy of the list of messages. After calling the func-
tion, print both of your lists to show that the original list has retained its messages.

Oct 2025
@jmerort
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
sent_messages = show_messages(messages[:]) # If you use slice notation, a copy of the list is passed

print(f"Proof that all messages remain:\nOriginal list: {messages}\nSent message list: {sent_messages}")