import os 
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 

def decode_file(file_name, decoded_string):
    # print("\n=======================================")
    # print(f"{Fore.GREEN}Writing Decoded String to New File...{Style.RESET_ALL}")
    # print("=======================================\n")

    # Write decoded contents to a new file:
    with open(f"{file_name}_decrypted.txt", "w") as decrypted_file:
        decrypted_file.write(decoded_string) 

    print("\n=============================")
    print(f"{Fore.GREEN}Decryption Process - Complete{Style.RESET_ALL}")
    print("=============================")
    print(f"Decrypted File Name: {Fore.YELLOW}{decrypted_file.name}{Style.RESET_ALL}")
    print(f"Decrypted Data: \n{Fore.RED}{decoded_string}{Style.RESET_ALL}")


    print("\n==============================")
    print(f"{Fore.GREEN}Deleting Encrypted Files & Key{Style.RESET_ALL}")
    print("==============================")
    print(f"Deleted: {Fore.RED}{file_name}{Style.RESET_ALL}{Fore.YELLOW}_encrypted{Style.RESET_ALL}{Fore.RED}.txt{Style.RESET_ALL}")
    print(f"Deleted: {Fore.RED}{file_name}{Style.RESET_ALL}{Fore.YELLOW}.key{Style.RESET_ALL}\n")
    os.remove(f"{file_name}_encrypted.txt")  # Delete encrypted copy.
    os.remove(f"{file_name}.key")  # Delete keyfile.