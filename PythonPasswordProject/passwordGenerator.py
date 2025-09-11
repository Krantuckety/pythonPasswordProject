import random
import string
from collections import Counter

# Function to generate a password
def generatePassword(length: int, useNumbers: bool, useSymbols: bool, minimizeRepeats: bool):
    # Declare variables
    chars = string.ascii_letters
    passwordStrength = 0

    # If password is long enough, change the number of allowed repeat characters
    match length:
        case x if x > 1 and x < 16:
            maxRepeat = 1   # A character can be repeated 1 time
        case x if x > 16 and x < 32:
            maxRepeat = 2   # A character can be repeated 2 times
        case x if x > 32:
            maxRepeat = 3   # A character can be repeated 3 times

    # Check to include numbers in the password
    if useNumbers:
        chars = chars + string.digits
        passwordStrength += 1
    # Check to include special symbols in the password
    if useSymbols:
        chars = chars + string.punctuation
        passwordStrength += 1
    # Check to minimize the number of repeats in the password
    if minimizeRepeats:
        password = generatePasswordNoRepeats(length, chars, maxRepeat)
        return password
    
    password = ''.join(random.choice(chars) for _ in range(length))

    return password

# Function to generate the password with minimized repeat characters
def generatePasswordNoRepeats(length: int, chars: string, maxRepeat: int):
    password = []
    counts = Counter()

    while len(password) < length:
        # Check if char has been repeated 2 times or not
        usableChars = [c for c in chars if counts[c] < maxRepeat]

        if not usableChars:
            raise ValueError("Not enough unique characters to meet repeat constraints")

        c = random.choice(usableChars)
        password.append(c)
        counts[c] +=1

    return (''.join(password))

def outputPasswordStrength(strengthRating: int):
    match strengthRating:
        case 0 | 1: 
            print("\nPassword Strength: WEAK")
