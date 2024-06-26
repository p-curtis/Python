import os 
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 

from decrypt_string import decrypt_string
from decode_string import decode_string
from decode_file import decode_file

def decrypt():

    #----Open/Read File & Extract Text as String----    
    file_selection = ""
    file_name = ""
    def grab_file_contents():
        # nonlocal string_conversion
        nonlocal file_selection
        nonlocal file_name
        print(f"\nCurrent Working Directory is: {os.getcwd()}")
        print(f"Directory Objects are: {os.listdir(os.getcwd())}\n")
        while True:
            try:
                print("File 1 or File 2?")
                choices = (f"Make a selection:\n{Fore.YELLOW}01.{Style.RESET_ALL} hello_encrypted.txt\n{Fore.YELLOW}02.{Style.RESET_ALL} multi_line_string_encrypted.txt")
                print(choices)
                selection = str(input("Choose a number based off the selection above [1 or 2]: "))
                if selection in ["1", "01"]:
                    file_selection = "hello_encrypted.txt"
                    break
                elif selection in ["2", "02"]:
                    file_selection = "multi_line_string_encrypted.txt"
                    break
                else:
                    os.system('clear')  # Expecting a Linux System. Performs a CLEAR using the OS Module.
                    print(f"{Fore.RED}Choose a valid selection (no spaces, no letters).{Style.RESET_ALL}")
                    pass
            except KeyboardInterrupt:  # Triggers on Keyboard Interrupt (^C) / (CTRL+C)
                print(f"{Fore.YELLOW}\nInterrupted by User{Style.RESET_ALL}")
                os.sys.exit()

        open_file = open(f"{file_selection}","r")
        read_file = open_file.readlines()
        open_file.close()

        # Remove extension (last 14 characters. Example: "_encrypted.txt")
        file_name = file_selection[:-14]
        print(f"\nText contents of selected file are:\n{Fore.YELLOW}{read_file}{Style.RESET_ALL}")
        return(file_selection, file_name)

    grab_file_contents()
    # Placeholder for decryption
    decrypted_data = decrypt_string(file_selection, file_name)
    decoded_string = decode_string(decrypted_data)
    decode_file(file_name, decoded_string)

# decrypt()
