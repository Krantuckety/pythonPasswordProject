# Dependencies
import string
import random
# Access passwordGenerator.py
from passwordGenerator import generatePassword

def main():
    # Greeting
    print("🔑 Welcome to Noah Ferenczhalmys Random Password Generator / Strength Tester🔑")

    while True:
        # Prompt for how long password should be
        while(True):
            length = int(input("Enter password length: "))
            if length < 99:
                break
            print("Password length to long, input a number smaller than 99")


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

        # Prompt for if
        userInput = (input("Do you want minimize repeat characters in your password? (Y/N): "))
        if userInput.lower() == "y":
            minimizeRepeats = True      # Characters can only be repeated 1-3 times based on length
        else:
            minimizeRepeats = False     # Characters can be repeated infinite times

        # Generate password
        password = generatePassword(length, useNumbers, useSymbols, minimizeRepeats)
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