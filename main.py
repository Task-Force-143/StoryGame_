import random

def choose_door():
    print("Choose a door: 1 or 2")
    choice = input()
    return int(choice)

def play_game():
    correct_door = random.randint(1, 2)
    
    print("Welcome to the Two-Door Game!")
    print("Behind one door is success, and behind the other is failure.")
    
    user_choice = choose_door()
    
    if user_choice == correct_door:
        print("Congratulations! You chose the correct door. You win!")
    else:
        print(f"Sorry, you chose the wrong door. The correct door was {correct_door}. Better luck next time!")

if __name__ == "__main__":
    play_game()
   for w in "" 
for m in range(15):
    print(m)
    