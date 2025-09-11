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
        case x if x > 16 and x < 22:
            maxRepeat = 2   # A character can be repeated 2 times
            passwordStrength += 1       # Add 1 point to the passwords Strength
        case x if x > 22 and x < 32:
            maxRepeat = 2   # A character can be repeated 2 times
            passwordStrength += 3       # Add 2 points to the passwords Strength
        case x if x > 32:
            maxRepeat = 3   # A character can be repeated 3 times
            passwordStrength += 4       # Add 3 points to the passwords Strength

    # Check to include numbers in the password
    if useNumbers:
        chars = chars + string.digits
    # Check to include special symbols in the password
    if useSymbols:
        chars = chars + string.punctuation
        if useNumbers:
            passwordStrength += 1       # Add 1 point to the passwords Strength
    # Check to minimize the number of repeats in the password
    if minimizeRepeats:
        password = generatePasswordNoRepeats(length, chars, maxRepeat)
        passwordStrength += 1       # Add 1 point to the passwords Strength
        # Output password Strength
        outputPasswordStrength(passwordStrength)
        return password
    
    password = ''.join(random.choice(chars) for _ in range(length))
    # Output password Strength
    outputPasswordStrength(passwordStrength)
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

# Function to assess the Strength Rating of a password and tell the user about it
def outputPasswordStrength(strengthRating: int):
    # Note: Password length is the greatest feature in making a strong password
    match strengthRating:
        case 0 | 1: 
            print("\nPassword Strength: VERY WEAK" + "\nTip: Try making your password longer than 16 characters")
        case 2:
            print("\nPassword Strength: WEAK")
        case 3:
            print("\nPassword Strength: MEDIUM")
        case 4:
            print("\nPassword Strength: STRONG")
        case 5 | 6:
            print("\nPassword Strength: VERY STRONG")
