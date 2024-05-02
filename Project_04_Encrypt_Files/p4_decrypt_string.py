import os 
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 
from cryptography.fernet import Fernet  # https://cryptography.io/en/latest/fernet/
    # https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/

# NOTE: https://www.reddit.com/r/learnpython/comments/cro91g/reading_fernet_key_from_file/ 
def decrypt_string(file_selection, file_name):

    print("\n===========================")
    print(f"{Fore.GREEN}Decryption Process - Begins{Style.RESET_ALL}")
    print("===========================")# Open & Read Key File:

    with open(f"{file_name}.key", "rb") as key_file:
        key = key_file.read()
        print(f"Sanity Checking Key: {key}")

    fernet = Fernet(key)

    # Open & Read Encrypted Contents:
    with open(f"{file_selection}", "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
        # print(f"Sanity Checking Data to be Decrypted: {encrypted_data}")

    decrypted_data = fernet.decrypt(encrypted_data)
    print(f"Decrypted Contents: {decrypted_data}")
    return(decrypted_data)

    # decrypt_string(file_selection)