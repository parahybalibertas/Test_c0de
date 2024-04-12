###Useful for generating strong passwords offline###

import string
import random

# Function to generate a password
def generate_password(length, include_numbers, include_lowercase, include_uppercase, include_symbols, exclude_similar):
    # Define character sets
    numbers = '23456789' if exclude_similar else string.digits
    lowercase = 'abcdefghjkmnpqrstuvwxyz' if exclude_similar else string.ascii_lowercase
    uppercase = 'ABCDEFGHJKLMNPQRSTUVWXYZ' if exclude_similar else string.ascii_uppercase
    symbols = '!";#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
    characters = ''

    # Include character sets based on user preferences
    if include_numbers:
        characters += numbers
    if include_lowercase:
        characters += lowercase
    if include_uppercase:
        characters += uppercase
    if include_symbols:
        characters += symbols

    # Ensure at least one character from each selected set is included
    password_characters = []
    if include_numbers:
        password_characters.append(random.choice(numbers))
    if include_lowercase:
        password_characters.append(random.choice(lowercase))
    if include_uppercase:
        password_characters.append(random.choice(uppercase))
    if include_symbols:
        password_characters.append(random.choice(symbols))

    # Fill the rest of the password length with random characters from the combined set
    password_characters += random.choices(characters, k=length - len(password_characters))
    random.shuffle(password_characters)  # Shuffle to ensure randomness
    password = ''.join(password_characters)

    return password

# Main program to interact with the user and generate a password
def main():
    print("Welcome to the Password Generator!")

    # Ask user for password preferences
    while True:
        length = int(input("Define the length of your password (12-50): "))
        if 12 <= length <= 50:
            break
        else:
            print("Please enter a length between 12 and 50.")

    include_numbers = input("Do you want it to include numbers? (yes/no): ").lower() == 'yes'
    include_lowercase = input("Do you want it to include lowercase characters? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Do you want it to include uppercase characters? (yes/no): ").lower() == 'yes'
    include_symbols = input("Do you want it to include symbols (!\";#$%&'()*+,-./:;<=>?@[]^_`{|}~)? (yes/no): ").lower() == 'yes'
    exclude_similar = input("Do you want the password not to have Similar Characters (like i, l, 1, L, o, 0, O, etc.)? (yes/no): ").lower() == 'yes'

    # Generate and display the password
    password = generate_password(length, include_numbers, include_lowercase, include_uppercase, include_symbols, exclude_similar)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
