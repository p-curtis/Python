import os 
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 
from cryptography.fernet import Fernet  # https://cryptography.io/en/latest/fernet/
    # https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/

def encrypt_string(file_selection):
    def fernet(file_selection):
        # Remove extension (last 4 characters. Example: ".txt")
        file_name = file_selection[:-4]

        # Generating Key & Storing Key as File
        key = Fernet.generate_key()
        with open(f"{file_name}.key", "wb") as filekey:  # https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
            filekey.write(key)
        
        fernet = Fernet(key)

        print("\n===========================")
        print(f"{Fore.GREEN}Encryption Process - Begins{Style.RESET_ALL}")
        print("===========================")

        # Opening the file so contents can be encrypted:
        with open(f"{file_selection}_temp.txt", "rb") as file:
            original_data = file.read()
            print(f"Data to be Encrypted (Byte Form): {original_data}")
        os.remove(f"{file_selection}_temp.txt")  # Delete _temp.txt
        encrypted_data = fernet.encrypt(original_data)  # Encrypt original_data using Fernet

        # Writing Encrypted Data to NEW file
        with open(f"{file_name}_encrypted.txt", "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
        # # Writing Encrypted Data to EXISTING file
        # with open(f"{file_selection}", "wb") as encrypted_file:
        #     encrypted_file.write(encrypted_data)

        print("\n=============================")
        print(f"{Fore.GREEN}Encryption Process - Complete{Style.RESET_ALL}")
        print("=============================")
        print(f"Encrypted File Name: {Fore.YELLOW}{encrypted_file.name}{Style.RESET_ALL}")
        print(f"Encrypted Data: {Fore.RED}{encrypted_data}{Style.RESET_ALL}\n")
        
    fernet(file_selection)

# encrypt_string(file_selection)