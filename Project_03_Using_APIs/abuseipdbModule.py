import os
import requests
import json
import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 
from dotenv import load_dotenv

load_dotenv()
ABUSEIPDB_API_KEY= (os.getenv("ABUSEIPDB_API_KEY"))

def abuseipdb_get(ip):

    # From AbuseIPDB Site:
    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {
        'ipAddress': ip
    }
    headers = {
        'Accept': 'application/json',
        'Key': ABUSEIPDB_API_KEY
    }
    response = requests.get(url=url, headers=headers, params=querystring)
    abuse_response = response.json()

    # Parse Data from API Response.
    abuse_ip_address = abuse_response['data']['ipAddress']
    abuse_confidence_score = abuse_response['data']['abuseConfidenceScore']
    abuse_country_code = abuse_response['data']['countryCode']
    abuse_isp = abuse_response['data']['isp']

    # Conditional Formatting for Verdict.
    if abuse_confidence_score <= 25:
        verdict = f"{Fore.GREEN}Benign{Style.RESET_ALL}"
    elif abuse_confidence_score >= 75:
        verdict = f"{Fore.RED}Malicious{Style.RESET_ALL}"
    elif abuse_confidence_score > 25 or abuse_confidence_score < 75:
        verdict = f"{Fore.YELLOW}Suspicious{Style.RESET_ALL}"
    abuse_output = (f"#### {Fore.YELLOW}Abuse IPDB Output{Style.RESET_ALL} ####\nIP Address: {str(abuse_ip_address)}\nCountry: {str(abuse_country_code)}\nISP: {str(abuse_isp)}\nConfidence Score (0-100): {str(abuse_confidence_score)}\nVerdict: {str(verdict)}\n")
    print(abuse_output)
    return

#abuseipdb_get()