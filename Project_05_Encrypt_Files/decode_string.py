# This module is to decode strings to the following:
# From a hex value list to integers
# Transform each integer into its character representation
# Join the list values together into a string

import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 

#----Transform Hex to Integers----
def decode_string(decrypted_data):

    #----Transform Bytes to String (Hex)----
    decode_byte_to_hex = ""
    def byte_to_hex(decrypted_data):
        nonlocal decode_byte_to_hex
        strip_strings = decrypted_data.decode("utf-8")
        decode_byte_to_hex = strip_strings.strip("b").strip("[]").replace("'", "").split(", ")
        print(f"Conversion - Byte to Hex: {decode_byte_to_hex}")

    #----Transform Hex to Integers----
    decode_hex_to_integer = ""
    def hex_to_integer(decode_byte_to_hex):
        nonlocal decode_hex_to_integer
        decode_hex_to_integer = []
        for d in decode_byte_to_hex:  # Convert Hex to Integer
            decode_remove_hex_prefix = d.lstrip("0x") # Removes "0x" prefix from hex values
            # print(f"Sanity Check - Remove Hex Prefix: {decode_remove_hex_prefix}")  # Debugging
            decode_integer_convert = int(decode_remove_hex_prefix, 16) # Converts hex values to decimal integer values
            # print(f"Sanity Check - Converts Hex to Ints: {decode_integer_convert}")  # Debugging
            decode_hex_to_integer.append(decode_integer_convert)
        print(f"Conversion - Hex to Integers: {decode_hex_to_integer}")

    #----Transform Integers to Characters----
    decode_integer_to_char = ""
    def integer_to_char(decode_hex_to_integer):
        nonlocal decode_integer_to_char
        decode_integer_to_char = []
        for d in decode_hex_to_integer:
            decode_integer_to_byte = chr(d)
            decode_integer_to_char.append(decode_integer_to_byte)
        print(f"Conversion - Integers to Characters: {decode_integer_to_char}")

    #----Join Characters Back into a String----
    decoded_string = ""
    def char_to_string(decode_integer_to_char):
        nonlocal decoded_string
        decoded_string = ''.join(decode_integer_to_char)
        print(f"Decoded Raw String:\n{decoded_string}")
        return(decoded_string)

    #----Decoding Process----
    print("\n=======================")
    print(f"{Fore.GREEN}Decoding Process Begins{Style.RESET_ALL}")
    print("=======================")
    byte_to_hex(decrypted_data)
    hex_to_integer(decode_byte_to_hex)
    integer_to_char(decode_hex_to_integer)
    char_to_string(decode_integer_to_char)
    return(decoded_string)

# decode_string(decrypted_data)