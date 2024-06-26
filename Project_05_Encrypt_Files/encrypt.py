import os 
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 
# Custom Module
from encode_string import encode_string 
from encode_file import encode_file
from encrypt_string import encrypt_string

def encrypt():

    #----Open/Read File & Extract Text as String----    
    string_conversion = ""
    file_selection = ""
    def grab_file_contents():
        nonlocal string_conversion
        nonlocal file_selection
        print(f"\nCurrent Working Directory is: {os.getcwd()}")
        print(f"Directory Objects are: {os.listdir(os.getcwd())}\n")
        while True:
            try:
                print("File 1 or File 2?")
                choices = (f"Make a selection:\n{Fore.YELLOW}01.{Style.RESET_ALL} hello.txt\n{Fore.YELLOW}02.{Style.RESET_ALL} multi_line_string.txt")
                print(choices)
                selection = str(input("Choose a number based off the selection above [1 or 2]: "))
                if selection in ["1", "01"]:
                    file_selection = "hello.txt"
                    break
                elif selection in ["2", "02"]:
                    file_selection = "multi_line_string.txt"
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
        string_conversion = ''.join(read_file)
        print(f"\nText contents of selected file are:\n{Fore.YELLOW}{string_conversion}{Style.RESET_ALL}")
        return(string_conversion, file_selection)

    grab_file_contents()
    hex_list = encode_string(string_conversion)
    encode_file(hex_list, file_selection)
    encrypt_string(file_selection)

# encrypt()
