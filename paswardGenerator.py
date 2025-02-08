import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."
    
    characters =   string.ascii_letters+ string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(length))
except ValueError:
    print("Invalid input! Please enter a valid number.")
