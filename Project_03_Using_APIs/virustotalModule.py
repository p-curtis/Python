import os
import requests
import json
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 
from dotenv import load_dotenv

load_dotenv()
VIRUSTOTAL_API_KEY= (os.getenv("VIRUSTOTAL_API_KEY"))

def virustotal_get(ip):

    #From VT Site:
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {
        "accept": "application/json",
        "x-apikey": VIRUSTOTAL_API_KEY
    }
    response = requests.get(url, headers=headers)
    vt_response = response.json()

    vt_ip_address = vt_response['data']['id']
    vt_risk = vt_response['data']['attributes']['last_analysis_stats']
    vt_country_code = vt_response['data']['attributes']['country']

    # Conditional Formatting for Verdict.
    if vt_risk['malicious'] in [1,2]:
        verdict = f"{Fore.YELLOW}Suspicious{Style.RESET_ALL}"
    elif vt_risk['malicious'] >= 3:
        verdict = f"{Fore.RED}Malicious{Style.RESET_ALL}"
    elif vt_risk['malicious'] == 0:
        verdict = f"{Fore.GREEN}Benign{Style.RESET_ALL}"
        
    vt_output = (f"#### {Fore.YELLOW}VirusTotal Output{Style.RESET_ALL} ####\nIP Address: {str(vt_ip_address)}\nCountry: {str(vt_country_code)}\nAV Engine Analysis: {str(vt_risk)}\nVerdict: {str(verdict)}\n")
    print(vt_output)
    return

#virustotal_get()