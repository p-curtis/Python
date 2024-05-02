import os
import requests
import json
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 
from dotenv import load_dotenv

load_dotenv()
PULSEDIVE_API_KEY= (os.getenv("PULSEDIVE_API_KEY"))

def pulsedive_get(ip):

    #From PulseDive Site:
    url = f'https://pulsedive.com/api/explore.php?q=ioc%3D{ip}&limit=10&pretty=1&key={PULSEDIVE_API_KEY}'
    response = requests.get(url)
    pulse_response = response.json()

    # If the output is a blank list ("[]")
    pulse_error = pulse_response['results']
    if pulse_error == []:
        pulse_output = f"#### {Fore.YELLOW}PulseDive Output{Style.RESET_ALL} ####\nNo data found for this entry: {ip}\n"

    # Parse Data from API Response.
    else:
        pulse_ip_address = pulse_response['results'][0]['indicator']
        pulse_risk = pulse_response['results'][0]['risk']
        pulse_country_code = pulse_response['results'][0]['summary']['properties']['geo']['countrycode']
        pulse_isp = pulse_response['results'][0]['summary']['properties']['geo']['org']
        
        # Conditional Formatting for Verdict.
        if pulse_risk in "low":
            verdict = f"{Fore.GREEN}Benign{Style.RESET_ALL}"
        elif pulse_risk in "medium":
            verdict = f"{Fore.YELLOW}Suspicious{Style.RESET_ALL}"
        elif pulse_risk in "high":
            verdict = f"{Fore.RED}Malicious{Style.RESET_ALL}"
        pulse_output = (f"#### {Fore.YELLOW}PulseDive Output{Style.RESET_ALL} ####\nIP Address: {str(pulse_ip_address)}\nCountry: {str(pulse_country_code)}\nISP: {str(pulse_isp)}\nRisk Score (Low/Med/High): {str(pulse_risk)}\nVerdict: {str(verdict)}\n")

    print(pulse_output)
    return

#pulsedive_get()