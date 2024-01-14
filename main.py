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

    registered_users[sign_us] = sign_us

elif loin_screen == "Credits":
    print("CID")

else:
    print("idk wht u trying to write am program dum")



#---------------------#


#-----story part-----#






#--------------------#