"""
Author: p-curtis
Date: 2024-04-30
Version: v0.0.1

To Do: 
1. Add Logic to "decrypt()". If there is no file_name with a ".key" file AND an "_encrypted.txt", throw an error saying that there must be both of these to continue. 
2. Add logic to identify if the proper key is being used for the operations. Not sure how I'd go about doing this at this point in time.
"""

import os 
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 

# from temp_proj4 import temp # Custom Module
from p4_encrypt import encrypt # Custom Module
from p4_decrypt import decrypt # Custom Module


def main():
    #----Create Directory to Perform Operations----
    def setup_actions():
        new_dir = "Proj4_Operations_Folder"
        try:
            if not os.path.exists(new_dir):
                print(f"\nOperations Folder Not Found. New Folder Created:\"{Fore.YELLOW}{new_dir}{Style.RESET_ALL}\". Files {Fore.RED}MUST{Style.RESET_ALL} be in this directory!!!\n")
                os.makedirs(new_dir)
            elif os.path.isdir(new_dir):
                print(f"\n{Fore.GREEN}The Operations Folder is already created{Style.RESET_ALL}.\n")

            os.chdir(new_dir)
            print(f"Your files must be in this \"{Fore.YELLOW}{os.getcwd()}{Style.RESET_ALL}\" Directory!!!. \nIf they are not, please press \"CTRL+C\" to quit the program and move them.")
        except KeyboardInterrupt:  # Triggers on Keyboard Interrupt (^C) / (CTRL+C)
            print(f"{Fore.YELLOW}\nInterrupted by User{Style.RESET_ALL}")
            os.sys.exit()

    ## NOTE: Goal is to have the files in the pwd printed, accepted as variables, drawn out as a number selection and let the user input select the file. 
    def selection():
        while True:
            try:
                print("\nEncrypt or Decrypt?")
                choices = (f"Make a selection:\n{Fore.YELLOW}01.{Style.RESET_ALL} Encrypt.\n{Fore.YELLOW}02.{Style.RESET_ALL} Decrypt.")
                print(choices)
                selection = str(input("Choose a number based off the selection above [1 or 2]: "))
                if selection in ["1", "01"]:
                    encrypt()
                    break
                elif selection in ["2", "02"]:
                    decrypt()
                    break
                else:
                    os.system('clear')  # Expecting a Linux System. Performs a CLEAR using the OS Module.
                    print(f"{Fore.RED}Choose a valid selection (no spaces, no letters).{Style.RESET_ALL}")
                    pass
            except KeyboardInterrupt:  # Triggers on Keyboard Interrupt (^C) / (CTRL+C)
                print(f"{Fore.YELLOW}\nInterrupted by User{Style.RESET_ALL}")
                os.sys.exit()

    setup_actions()
    selection()

main()
