# Dependencies
import string
import random
# Access passwordGenerator.py
from passwordGenerator import generatePassword

def main():
    print("Welcome to Noah Ferenczhalmys Random Password Generator")
    # Prompt to ask if numbers should be included
    userInput = string(input("Do you want numbers in your password? (Y/N)"))             
    if userInput.lower() == "y":
        useNumbers = True
    else:
        useNumbers = False
    # Prompt to ask if special characters should be included
    userInput = String(input("Do you want special characters in your password? (Y/N)"))
    if userInput.lower() == "y":
        useSymbols = True
    else:
        useSymbols = False
    length = int(input("Enter password length: "))
    # Generate password
    password = generatePassword(length, useNumbers, useSymbols)
    # Print password
    print("your randomly generated password is: ", password)

    if __name__ == "__main__":
        main()