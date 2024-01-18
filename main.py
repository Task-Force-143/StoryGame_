#----modules---------#
import os
import datetime
import sys
import time
#----------------------

#-----login-----sphinx#


registered_users = {"user1": "password1", "user2": "password2"}

print("Welcome to this program")
time.sleep(1)
print("Wait, not actually a program but a game.")
time.sleep(2)

login_screen = input("Login\nSign Up\nCredits\n")

if login_screen == "Login":
    login_us = input("Username: ")
    login_pas = input("Password: ")

    if login_us in registered_users and registered_users[login_us] == login_pas:
        print("Login Successful")

    else:
        print("Wrong Password")
        sys.exit()

elif login_screen == "Sign Up":
    sign_us = input("Username: ")
    sign_pas = input("Password: ")
    registered_users[sign_us] = sign_pas
    print("Registration Successful")

elif login_screen == "Credits":
    print("CID")

else:
    print("I don't know what you're trying to write. I am just a program, dumb.")
    sys.exit()

#---------------------#


#-----story part-----#
time.sleep(2)
print("You open your eyes to find yourself in a dimly lit room. The air is thick with an eerie silence. As you stand up, you notice two large wooden doors in front of you. One on the left and the other on the right. The room seems to be pulsating with a mysterious energy.")
time.sleep(4)
print("Door 1: You cautiously approach the first door. It's adorned with intricate carvings and emits a soft glow. The handle is cool to the touch. With a deep breath, you turn the handle and step through.")
time.sleep(3)
print("Door 2: The second door is plain, almost unremarkable compared to the first. As you reach for the handle, you feel a strange warmth emanating from it. Hesitating only briefly, you push the door open and step into the unknown.")\
time.sleep(4)
door_choice = input("Choose the door: ")
if door_choice == '1':
    time.sleep(3)
    print("Beyond Door 1: The moment you step through Door 1, you find yourself in a vast chamber filled with glittering treasures. Jewels of every color imaginable, golden statues, and chests overflowing with coins surround you. You're in a room fit for a king. However, as you start exploring, you hear a low growl. A guardian creature, part lion, part eagle, emerges from the shadows. It eyes you suspiciously. Now you must decide whether to face the guardian or make a hasty retreat.")
    time.sleep(3)
elif door_choice == '2':
    time.sleep(2)
    print("Beyond Door 2: Upon entering through Door 2, you find yourself in a magical garden bathed in a soft, otherworldly light. Colorful flowers of every shape and size bloom around you, and butterflies flutter in the air. In the center of the garden, a majestic unicorn grazes peacefully. The unicorn raises its head, acknowledging your presence. It begins to speak, revealing that it can answer one question about your future. You must carefully choose your question, as the unicorn's insight could shape your destiny.")
    time.sleep(3)
import time

time.sleep(4)
guardian_decision = input("The guardian challenges you to prove your worthiness. Solve a riddle or perform a task to gain access to even greater treasures hidden within the room. Do you want to solve a riddle or perform a task? (Type 'riddle' or 'task'): ")

if guardian_decision.lower() == 'riddle':
    print("The guardian presents you with a riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'")
    time.sleep(3)
    answer = input("Your answer: ")

    if answer.lower() == 'an echo':
        print("Correct! The guardian nods in approval, and a hidden door opens to reveal even greater treasures.")
    else:
        print("Incorrect!the guardian is unimpressed, and the adventure ends here .")

elif guardian_decision.lower() == 'task':
    print("The guardian tasks you with arranging a set of enchanted crystals in a specific pattern.")
    time.sleep(3)
    print("You see three crystals of different colors: red, blue, and green.")
    time.sleep(3)
    print("Arrange them in the correct order to unlock the hidden door.")
    time.sleep(3)

    # Ask the player to input their arrangement
    arrangement = input("Enter the order of colors (e.g., 'red blue green'): ")
    time.sleep(3)

    # Check if the arrangement is correct
    correct_arrangement = 'red blue green'
    if arrangement.lower() == correct_arrangement:
        print("Well done! The guardian is pleased, and a hidden door opens to reveal even greater treasures.")
    else:
        print("Incorrect arrangement! The guardian is unimpressed, and the adventure ends here.")

else:
    print("Invalid choice. The guardian is unimpressed, and the adventure ends here.")
    import time
print("Stage 4: Enchanted Path (Door 2):")
print("Your question to the unicorn leads to an enchanted path. As you walk, the surroundings transform, presenting you with visions of possible futures.")
print("Choose wisely, as your decisions here may impact your journey.")

time.sleep(3)
decision = input("You come across a crossroads. Do you want to go left or right? (Type 'left' or 'right'): ")

if decision.lower() == 'left':
    print("You chose the left path. The air shimmers, and you feel a sense of tranquility as you continue on your journey.")

elif decision.lower() == 'right':
    print("You chose the right path. The surroundings become more mysterious, and you sense a hidden power in the air and your adventure ends here.")
    # Add more story or challenges for the right path if needed

else:
    print("Invalid choice. The path becomes unclear, and you find yourself lost in the enchantment and your adventure ends here.")
    print("idk)
