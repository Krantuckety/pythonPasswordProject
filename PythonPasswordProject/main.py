# Dependencies
import string
import random
# Access passwordGenerator.py
from passwordGenerator import generatePassword

def main():
    # Greeting
    print("🔑 Welcome to Noah Ferenczhalmys Random Password Generator 🔑")

    while True:
        # Prompt for how long password should be
        length = int(input("Enter password length: "))

        # Prompt for if numbers should be included
        userInput = (input("Do you want numbers in your password? (Y/N): "))             
        if userInput.lower() == "y":
            useNumbers = True
        else:
            useNumbers = False

        # Prompt for if special characters should be included
        userInput = (input("Do you want special characters in your password? (Y/N): "))
        if userInput.lower() == "y":
            useSymbols = True
        else:
            useSymbols = False

        # Generate password
        password = generatePassword(length, useNumbers, useSymbols)
        # Print password
        print("your randomly generated password is: ", password)
        
        # Prompt for if user wants to generate another password
        repeat = input("\nDo you want to generate another password? (Y/N): ")
        
        if repeat.lower() != "y":
            print("Thanks for trying out my program!!")
            break # Exit loop

# Call to run the main method
if __name__ == "__main__":
    main()