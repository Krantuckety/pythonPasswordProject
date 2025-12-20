# Dependencies
import math
import random
import string
from collections import Counter

# Function to generate a password
def generatePassword(length: int, useNumbers: bool, useSymbols: bool, minimizeRepeats: bool):
    # Declare variables
    chars = string.ascii_letters
    passwordStrength = 0
    numPasswordCombinations = 52  # Start with letters only

    # If password is long enough, change the number of allowed repeat characters
    match length:
        case x if x > 1 and x < 16:
            maxRepeat = 1   # A character can be repeated 1 time
        case x if x > 16 and x < 22:
            maxRepeat = 2   # A character can be repeated 2 times
        case x if x > 22 and x < 32:
            maxRepeat = 2   # A character can be repeated 2 times
        case x if x > 32:
            maxRepeat = 3   # A character can be repeated 3 times

    # Check to include numbers in the password
    if useNumbers:
        chars = chars + string.digits
    # Check to include special symbols in the password
    if useSymbols:
        chars = chars + string.punctuation
    # Check to minimize the number of repeats in the password
    if minimizeRepeats:
        password = generatePasswordNoRepeats(length, chars, maxRepeat)
        # Output password Strength
        outputPasswordStrength(passwordStrength)
        return password
    
    password = ''.join(random.choice(chars) for _ in range(length))
    # Output password Strength
    outputPasswordStrength(passwordStrength)
    return password

def calculatePasswordEntropy(numCombinations: int):
    """
    Password Entropy Formula: (length) * log2(numCombinations)
    Below are some example calculations of entropy explaining how different parameters affect the entropy:
    EX1: 8 character password using only letters (52 characters) = 45.60 bits
    EX2: 8 character password using letters & numbers (62 characters) = 47.63 bits
    EX3: 8 character password using letters, numbers & symbols (94 characters) = 52.43 bits
    # The above demonstrates minuscule gains from nearly doubling the character set size. 
    EX4: 9 character password using only letters (52 characters) = 51.30 bits
    EX5: 9 character password using letters, numbers & symbols (94 characters) = 58.99 bits
    EX6: 13 character password using only letters (94 characters) = 85.21 bits
    # The above demonstrates significant gains by increasing password length, far greater than achieved by increasing character set size.
    # Therefore, focus on making passwords longer rather than just more complex.
    """
    entropy = math.log2(numCombinations)
    return entropy

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
def outputPasswordStrength(entropyRating: float):
    # Note: Password length is the greatest contributor to strength rating
    match entropyRating:
        case x if (0 <= x < 60): 
            print("\nPassword Strength: WEAK" + "\nTip: Try making your password longer than 16 characters")
        case x if (60 <= x < 80):
            print("\nPassword Strength: MEDIUM")
        case x if (80 <= x < 110):
            print("\nPassword Strength: STRONG")
        case x if (110 <= x):
            print("\nPassword Strength: VERY STRONG")
