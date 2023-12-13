#SHRISHTI SINGH
#CODSOFT Task 3 password generator

import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on user preference
    character_set = lowercase_letters + uppercase_letters + digits + special_characters

    # Check if the length is greater than 0
    if length <= 0:
        return "Password length should be greater than 0."

    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))

    return password

# Main program
try:
    desired_length = int(input("Enter the desired password length: "))
    generated_password = generate_password(desired_length)
    print(f"Generated Password: {generated_password}")
except ValueError:
    print("Invalid input. Please enter a valid password length (an integer).")