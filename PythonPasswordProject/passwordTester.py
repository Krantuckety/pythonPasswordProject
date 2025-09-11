# Dependencies
import string
from collections import Counter

def testPassword(password: string):
    print("This is a temp statement for the testPassword function")

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