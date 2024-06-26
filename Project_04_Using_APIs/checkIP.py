import os
import re
import requests
import json
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 

# These will be the main functions I'll use once I fix API parsing.
from virustotalModule import virustotal_get as vt
from abuseipdbModule import abuseipdb_get as abuse
from pulsediveModule import pulsedive_get as pulse

def main():
    ip = ""
    def check_IP():
        nonlocal ip
        #ip = "218.92.0.31" # Bad
        while True:
            try:
                ip = input(f"Type in an IP: ")
                #if not re.match("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$",ip): 
                if not re.match("((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.(25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.(25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.(25[0-5]|(2[0-4]|1\d|[1-9]|)\d))",ip):
                    # TODO: https://stackoverflow.com/questions/51691270/python-user-input-as-regular-expression-how-to-do-it-correctly
                    # TODO: https://stackoverflow.com/questions/33881152/validate-user-input-using-regular-expressions
                    print(f"{Fore.RED}You must submit a valid IP! Example: 1.1.1.1 to 255.255.255.255{Style.RESET_ALL}")
                    pass
                else:
                    os.system('clear')  # Expecting a Linux System. Performs a CLEAR using the OS Module.
                    break
            except KeyboardInterrupt:   # Triggers on Keyboard Interrupt (^C) / (CTRL+C)
                print(f"{Fore.YELLOW}\nInterrupted by User{Style.RESET_ALL}")
                os.sys.exit()
        
    def all_options(ip):
        vt(ip)
        abuse(ip)
        pulse(ip)

    def selection():
        while True:
            try:
                print(f"Your Query is for: {Fore.GREEN}{ip}{Style.RESET_ALL}")
                choices = f"\nMake a selection:\n{Fore.YELLOW}01.{Style.RESET_ALL} All of them.\n{Fore.YELLOW}02.{Style.RESET_ALL} VirusTotal\t- https://www.virustotal.com/\n{Fore.YELLOW}03.{Style.RESET_ALL} AbuseIPDB\t- https://www.abuseipdb.com/\n{Fore.YELLOW}04.{Style.RESET_ALL} PulseDive\t- https://pulsedive.com/\n"#print choices above.
                print(choices)
                selection = str(input("Choose a number based off the selection above [1-4]: "))
                if selection in ["1", "01"]:
                    all_options(ip)
                    break
                elif selection in ["2", "02"]:
                    vt(ip)
                    break
                elif selection in ["3", "03"]:
                    abuse(ip)
                    break
                elif selection in ["4", "04"]:
                    pulse(ip)
                    break
                else:
                    os.system('clear')  # Expecting a Linux System. Performs a CLEAR using the OS Module.
                    print(f"{Fore.RED}Choose a valid selection (no spaces, no letters).{Style.RESET_ALL}")
                    pass
            except KeyboardInterrupt:  # Triggers on Keyboard Interrupt (^C) / (CTRL+C)
                print(f"{Fore.YELLOW}\nInterrupted by User{Style.RESET_ALL}")
                os.sys.exit()

    check_IP()
    selection()

main()