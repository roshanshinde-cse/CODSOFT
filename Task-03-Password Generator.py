# Task-03-PasswordGenerator/password_generator.py

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=== Password Generator ===")
length = int(input("Enter desired password length: "))
print("Your strong password is:", generate_password(length))
