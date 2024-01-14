#----modules---------#
import os
import datetime
import time
#----------------------

#-----login-----sphnix#


registered_users = {"user1" : "password1", "user2": "password2"}

print("Welcome to this program")
time.sleep(1)
print("wait not actually a program a game ")
time.sleep(2)

loin_screen = input("Login\nSign Up\nCredit\n")

if loin_screen == "Login":
    login_us = input("Username: ")
    login_pas = input("Password: ")

    if login_us in registered_users and registered_users[login_us]:
        print("Login Successful")

    else:
        print("Wrong Password")
elif loin_screen == "Sign Up":
    sign_us = input("Username: ")
    sign_pas = input("Password: ")

<<<<<<< HEAD
<<<<<<< HEAD
if __name__ == "__main__":
     play_game()   
=======
>>>>>>> 22672c801e924f3344a8843531b1078fc3269bcf
=======
    registered_users[sign_us] = sign_us
>>>>>>> fd2eb34771bac8d1d5f05911964951da532f5582

<<<<<<< HEAD
<<<<<<< HEAD

=======
=======
elif loin_screen == "Credits":
    print("CID")

else:
    print("idk wht u trying to write am program dum")



>>>>>>> fd2eb34771bac8d1d5f05911964951da532f5582
#---------------------#


#-----story part-----#
print("You open your eyes to find yourself in a dimly lit room. The air is thick with an eerie silence. As you stand up, you notice two large wooden doors in front of you. One on the left and the other on the right. The room seems to be pulsating with a mysterious energy.")
print("Door 1: You cautiously approach the first door. It's adorned with intricate carvings and emits a soft glow. The handle is cool to the touch. With a deep breath, you turn the handle and step through.")
print("Door 2: The second door is plain, almost unremarkable compared to the first. As you reach for the handle, you feel a strange warmth emanating from it. Hesitating only briefly, you push the door open and step into the unknown.")
door_choice = input("Choose the door: ")
if door_choice == '1':
    print("Beyond Door 1: The moment you step through Door 1, you find yourself in a vast chamber filled with glittering treasures. Jewels of every color imaginable, golden statues, and chests overflowing with coins surround you. You're in a room fit for a king. However, as you start exploring, you hear a low growl. A guardian creature, part lion, part eagle, emerges from the shadows. It eyes you suspiciously. Now you must decide whether to face the guardian or make a hasty retreat.")
elif door_choice == '2':
    print("Beyond Door 2: Upon entering through Door 2, you find yourself in a magical garden bathed in a soft, otherworldly light. Colorful flowers of every shape and size bloom around you, and butterflies flutter in the air. In the center of the garden, a majestic unicorn grazes peacefully. The unicorn raises its head, acknowledging your presence. It begins to speak, revealing that it can answer one question about your future. You must carefully choose your question, as the unicorn's insight could shape your destiny.")



#--------------------#
>>>>>>> 22672c801e924f3344a8843531b1078fc3269bc