#programmer James Maher
#Date: 3.12.2024
#Program: Password Generator
# resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import os

def hash_password(password, salt):
    # Combine password and salt
    salted_password = password.encode() + salt
    # Hash the salted password
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

def main():
    # Get password from user input
    password = input("Enter your password: ")

    # Generate a random salt
    salt = os.urandom(16)

    # Hash the password using the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed password:", hashed_password)

if __name__ == "__main__":
    main()
import hashlib
import os
import getpass

def hash_password(password, salt):
    # Combine password and salt
    salted_password = password.encode() + salt
    # Hash the salted password
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

def main():
    # Get password from user input without showing the characters
    password = getpass.getpass("Enter your password: ")

    # Generate a random salt
    salt = os.urandom(16)

    # Hash the password using the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed password:", hashed_password)

if __name__ == "__main__":
    main()