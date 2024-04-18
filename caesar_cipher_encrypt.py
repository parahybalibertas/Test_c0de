def caesar_cipher_encrypt(plaintext, shift):
    """
    Encrypts a plaintext using the Caesar Cipher.
    Each letter in the plaintext is shifted a certain number of places down the alphabet.

    :param plaintext: The original message that needs to be encrypted.
    :param shift: The number of places to shift each letter in the plaintext.
    :return: The encrypted message as ciphertext.
    """
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            # Calculate the shift for uppercase and lowercase separately
            offset = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Non-alphabetical characters are added unchanged
            encrypted_text += char
    return encrypted_text

# Interactive portion to guide the user through the encryption process
print("Welcome to the Caesar Cipher encryption tool!")
print("This tool will help you encrypt a message using the Caesar Cipher.")
print("In this cipher, each letter in your message is shifted a certain number of places down the alphabet.\n")

# Get user input for the plaintext and shift amount
plaintext = input("Enter the message you would like to encrypt: ")
shift = input("Enter the number of places to shift each letter in the message (1-25): ")

# Validate the shift input
while not shift.isdigit() or not 1 <= int(shift) <= 25:
    print("Invalid shift amount. It must be a number between 1 and 25.")
    shift = input("Please enter a valid shift amount (1-25): ")

shift = int(shift)  # Convert shift amount to integer

# Perform the encryption
encrypted_message = caesar_cipher_encrypt(plaintext, shift)

# Show the results to the user
print("\nOriginal message:", plaintext)
print("Shift amount:", shift)
print("Encrypted message:", encrypted_message)

print("\nEach letter in the original message has been shifted", shift, "places down the alphabet.")
print("For example, 'A' with a shift of 3 becomes:", caesar_cipher_encrypt('A', shift))
print("You can decrypt the message by shifting it back by the same amount using a decryption tool.")
