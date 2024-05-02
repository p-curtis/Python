import os
import requests
import json
import colorama                                         # Used for coloration of text. # REPO: https://pypi.org/project/colorama/ IDEA: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
from colorama import Fore, Style                        # Sets Foreground & Style Reset for Colorama. Seen by the {Fore.} and {Style.RESET_ALL} tags.
from dotenv import load_dotenv

load_dotenv()
THREATFOX_API_KEY= (os.getenv("THREATFOX_API_KEY"))

# def threatfox_get():

#     ip = "8.8.8.8"

#     # From ThreatFox https://github.com/abusech/ThreatFox:
#     url = 'https://api.abuseipdb.com/api/v2/check'
#     querystring = {
#         'ipAddress': ip
#     }
#     headers = {
#         'Accept': 'application/json',
#         #'Key': THREATFOX_API_KEY
#     }
#     response = requests.get(url=url, headers=headers, params=querystring)
#     decodedResponse = json.loads(response.text)
#     print(json.dumps(decodedResponse, sort_keys=True, indent=4))

# #------
#     pool = urllib3.HTTPSConnectionPool('threatfox-api.abuse.ch', port=443, maxsize=50)
#     data = {
#         'query':            'search_ioc',
#         'search_term':      sys.argv[1]

# #def threatfox_format():

# threatfox_get()