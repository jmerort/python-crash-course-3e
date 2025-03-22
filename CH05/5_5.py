# 5-5
# Alien Colors #3: Turn your if- else chain from Exercise 5-4 into an if- elif-
# else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
#   for the appropriate color alien.

# alien_color = "green"
# alien_color = "yellow"
alien_color = "red"
# alien_color = "blue" # you get nothing for these

if alien_color == "green":
    print("5 points!")
elif alien_color == "yellow":
    print("10 points!")
elif alien_color == "red": # I don't use an else to make sure other types of alien don't get the score of a red one
    print("15 points!")

