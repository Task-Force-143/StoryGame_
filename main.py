import time
import os

#------------------------------------------------------------------------------------------------

# Initialize an empty dictionary to store credentials
credentials = {}

# Load existing credentials from the file
try:
    with open('credentials.txt', 'r') as file:
        credentials = dict(line.strip().split(':') for line in file)
except FileNotFoundError:
    pass

# Main program loop
while True:
    # Display menu options
    print("\n1. Sign Up\n2. Login\n3. Quit")

    # Get user choice
    choice = input("Enter your choice (1/2/3): ")

    # Sign Up
    if choice == '1':
        print("Sign Up:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the username already exists
        if username in credentials:
            print("Username already exists. Please choose a different one.")
        else:
            # Add new credentials to the dictionary
            credentials[username] = password

            # Save the updated credentials to the file
            with open('credentials.txt', 'w') as file:
                for u, p in credentials.items():
                    file.write(f"{u}:{p}\n")

            print("Sign up successful!")

            while True:
                sign_up_wish = input("Are you new to this program? \nYes \nNo: ")
                if sign_up_wish.lower() == "yes":
                    # New Program starting for new players/clients

                    print("Hi wlcm to this program ")
                    

                    #pending
                    
                elif sign_up_wish.lower() == "no":
                    print("then u should have logged in ")
                    os.system("shutdown /s /t 1")
                else:
                    print("Invalid choice. Please enter 'Yes' or 'No'.")

    # Login
    elif choice == '2':
        print("Login:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the username and password match
        if username in credentials and credentials[username] == password:
            print("Login successful!")
        else:
            print("Invalid username or password. Please try again.")

    # Quit
    elif choice == '3':
        os.system("shutdown /s /t 1")

    # Invalid choice
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
