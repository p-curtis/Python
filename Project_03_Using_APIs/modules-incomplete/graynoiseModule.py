import os
import requests
import json
import colorama                                         # Used for coloration of text. # REPO: https://pypi.org/project/colorama/ IDEA: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
from colorama import Fore, Style                        # Sets Foreground & Style Reset for Colorama. Seen by the {Fore.} and {Style.RESET_ALL} tags.
from dotenv import load_dotenv

load_dotenv()
GRAYNOISE_API_KEY= (os.getenv("GRAYNOISE_API_KEY"))

def graynoise_get():
    
    ip = "8.8.8.8"
    
    # From Graynoise Site:
    url = "https://api.greynoise.io/v2/noise/quick/" + ip
    headers = {
        "accept": "application/json",
        "key": GRAYNOISE_API_KEY
    }
    response = requests.get(url, headers=headers)
    print(response.text)

#def graynoise_format():

graynoise_get()