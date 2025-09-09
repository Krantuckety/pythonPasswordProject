import random
import string

def getPasswordCharacteristics():
    print("Temp")

def generatePassword(length: int, useNumbers: bool,  useSymbols: bool):
    characters = string.ascii_letters
    if useNumbers:
        characters = characters + string.digits
    if useSymbols:
        characters = characters + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
