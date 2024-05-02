import os 
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 


def encode_file(hex_list, file_selection):
    print("\n=============================")
    print(f"{Fore.GREEN}Encode File Contents - Begins{Style.RESET_ALL}")
    print("=============================")

    # Transform Hex_list into a string:
    hex_list = str(hex_list)
    # return(hex_list)

    # # Simply write encoded strings to new file.
    with open(f"{file_selection}_temp.txt", "w") as file:
        encoded_content = file.write(hex_list) 
        print(f"Data Encoded to Bytes: {encoded_content}")

    # return(encoded_file)