import datetime
import time
import os

if os.path.exists("first_run.txt"):
    first_run = False
else:
    first_run = True

if first_run:
    time.sleep(3)
    print("Hi, welcome to this program made by Raghav Rawat")
    print("""
    .___  .____  __   __ _ __    _ .___   .____  .___  
    /   \\ /      |    |  | |\\   |  /   `  /      /   ` 
    |__-' |__.   |\\  /|  | | \\  |  |    | |__.   |    |
    |  \\  |      | \\/ |  | |  \\ |  |    | |      |    |
    /   \\ /----/ /    /  / |   \\|  /---/  /----/ /---/ 
    version - 0.1 beta
    """)
    time.sleep(3)
    print("loading..")
    time.sleep(2)
    print("loading...")
    time.sleep(1)
    print("loading....")
    time.sleep(2)
    print("loading......")
    time.sleep(1)
    print("loaded!")
    time.sleep(1)
    print("tada")
    print("ok")




    user_name = input("Please enter your username (this can't be reset *till now):  ")

    if user_name in ["Sphinx", "sphnix", "raghav", "Raghav"]:
        print(f"Hi {user_name} ")
        sphinx_command = input("Any orders for me today (yes/no): ")
        if sphinx_command in ["yes", "ye", "ya", "y"]:
            print("Game Stats, Real Life Stats, Reminders")
            response = input()

            if response == "game stats":
                print("See Stats, Set Stats, Clear Stats")
                custom_game = input()

                if custom_game == "Set Stats" or custom_game == "2":
                    game_stats = input("Please enter stats/reminders")

                if custom_game == "See Stats" or custom_game == "1":
                    print(game_stats)
                    if game_stats == "":
                        print("no current stats/reminders for games")

                if custom_game == "Clear Stats" or custom_game == "3":
                    game_stats = ""

            if response == ".iamok":
                print(".....")
                iamok = input()
                if iamok == ".iamnotok":
                    print("Oh, so you're here. Hi!")
                    time.sleep(2)
                    print("So you're feeling like quitting already.")
                    time.sleep(1)
                    print("Remember ....")
                    time.sleep(2)
                    print("Champions are not made in the days they feel like working. They are made in the days when they feel like quitting.")
                    time.sleep(1)
                    print("Hope this helps you, future me (:")
                    time.sleep(2)
                    print("Goodbye (:")

    else:
        print(f"Oh hi {user_name}, nice to meet you")
        time.sleep(2)
        print("...")
        time.sleep(2)
else:
    print("Welcome back!")

with open("first_run.txt", "w") as file:
    file.write("This is not the first run.")
