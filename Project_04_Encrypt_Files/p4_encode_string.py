# This module is to encode strings to the following:
# From a raw string (string literal?) to a per-character list.
# Transform each character into its ASCII Byte representation.
# Transform each ASCII value to an integer (decimal).
# Transform each integer to its hex value.

import colorama  # Used for coloration of text. 
from colorama import Fore, Style  # Sets Foreground {Fore.} & Style Reset 
                                  # {Style.RESET_ALL} tags for Colorama. 

def encode_string(string_conversion):
    #----Raw String----
    char_list = ""
    def raw_string(string_conversion):
        nonlocal char_list
        char_list = list(string_conversion)
        print(f"CHAR List: {char_list}")

    #----Transform Characters to ASCII Bytes----
    encode_char_to_byte = ""
    def char_to_byte(char_list):
        nonlocal encode_char_to_byte
        encode_char_to_byte = []
        for a in char_list:  # Convert chars into ASCII Bytes
            byte_convert = a.encode(encoding="ascii")
            encode_char_to_byte.append(byte_convert)
        print(f"Conversion - Characters to ASCII Bytes: {encode_char_to_byte}")

    #----Transform ASCII Bytes to Integers----
    encode_byte_to_integer = ""
    def byte_to_integer(encode_char_to_byte):
        nonlocal encode_byte_to_integer
        encode_byte_to_integer = []
        for b in encode_char_to_byte:  # Convert ASCII Bytes into Integers
            integer_convert = int.from_bytes(b, "big")  # https://www.geeksforgeeks.org/how-to-convert-bytes-to-int-in-python/
            encode_byte_to_integer.append(integer_convert)    
        print(f"Conversion - ASCII Bytes to Integers: {encode_byte_to_integer}")

    #----Transform Integers to Hex Values----
    hex_list = ""
    def integer_to_hex(encode_byte_to_integer):
        nonlocal hex_list
        encode_integer_to_hex = []
        for c in encode_byte_to_integer:  # Convert Integers into Hex
            hex_convert = hex(c)
            encode_integer_to_hex.append(hex_convert)
        hex_list = encode_integer_to_hex
        print(f"Conversion - Integers to Hex: {hex_list}")
        return(hex_list)

    #----Encoding Process Begins----
    print("\n======================")
    print(f"{Fore.GREEN}Encode String - Begins{Style.RESET_ALL}")
    print("======================")
    raw_string(string_conversion)
    char_to_byte(char_list)
    byte_to_integer(encode_char_to_byte)
    integer_to_hex(encode_byte_to_integer)
    return(hex_list)

# encode_string(string_conversion)