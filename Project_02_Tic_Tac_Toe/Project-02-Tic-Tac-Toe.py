# Project 2 (100 Points)

# For Project 2 we're making a tic-tac-toe game.
# You may use Internet resources, but your code should NOT be a copy of someone elses work.
# This is your project, so take pride in what you've learned, and write your own code.

# You will demonstrate your finished project, once it's completed.
# You should be able to show a working game, and explain how the code works.

# Bonus: Earn some kudos by adding some flavor to the program.
# Adding ASCII art, style elements, etc. will make your game unique.

# Grading Rubric...
# 1) Does the game work? (60 Points)
#   a) Demo walk-through.
#   b) Can either player win?
#   c) Can you get each type of win?... Diagonal, vertical, or horizontal?
#   d) Does the game detect when there is a tie?
#   e) Can a player crash the game if they enter invalid input?
# 2) Can you explain the code, and answer questions about the code? (40 Points)
#   a) How is the board state stored?
#   b) How is x/o selection verified?
#   c) How are the different win conditions determined?
#   d) How does the game determine which player won?
# 3) Does your game have any bonus flavor? (10 Points)
#   a) ASCII Art?
#   b) Screen refresh?
#   c) Current player displayed?
#   d) Winner message?
#   e) Screen refresh delays?
#   f) Other fancy features?

# ===================================================================================
# Author: Omnisophic
# Date: 2024-01-27
# Comments: Project 2 of 'Python Coding Hour' with brok3nwir3.
# ===================================================================================

import time                                             # Used for controling program flow (wait/sleep/etc.)
import os                                               # Used for calling OS-specific commands (clearing the terminal screen).
import colorama                                         # Used for coloration of text. # REPO: https://pypi.org/project/colorama/ IDEA: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
from colorama import Fore, Style                        # Sets Foreground & Style Reset for Colorama. Seen by the {Fore.} and {Style.RESET_ALL} tags.

def pregame():                                          # Master control flow for pregame functions.
    count = 0                                           # Used for ascii_animation and pregame_loop functions
    
    def ascii_animation(count):                         # ASCII Art Generated at: https://textkool.com/en/ascii-art-generator
        # Base Layer - All BLUE
        os.system('clear')                              # Expecting a Linux System. Performs a CLEAR using the OS Module.
        print(f"""{Fore.BLUE}
            ████████ ██  ██████               ████████  █████   ██████               ████████  ██████  ███████ 
               ██    ██ ██                       ██    ██   ██ ██                       ██    ██    ██ ██      
               ██    ██ ██          █████        ██    ███████ ██          █████        ██    ██    ██ █████   
               ██    ██ ██                       ██    ██   ██ ██                       ██    ██    ██ ██      
               ██    ██  ██████                  ██    ██   ██  ██████                  ██     ██████  ███████ 
                                                                                                               {Style.RESET_ALL}
            """)
        time.sleep(0.3)                                 # Sleeps for 1/3rd of a second.
        os.system('clear')                              # Expecting a Linux System. Performs a CLEAR using the OS Module.

        # 1st Movement - Top 3rd Green
        print(f"""{Fore.GREEN}
            ████████ ██  ██████               ████████  █████   ██████               ████████  ██████  ███████ 
               ██    ██ ██                       ██    ██   ██ ██                       ██    ██    ██ ██      {Style.RESET_ALL}{Fore.BLUE}
               ██    ██ ██          █████        ██    ███████ ██          █████        ██    ██    ██ █████ 
               ██    ██ ██                       ██    ██   ██ ██                       ██    ██    ██ ██      
               ██    ██  ██████                  ██    ██   ██  ██████                  ██     ██████  ███████ 
                                                                                                               {Style.RESET_ALL}
            """)
        time.sleep(0.3)                                 # Sleeps for 1/3rd of a second.
        os.system('clear')                              # Expecting a Linux System. Performs a CLEAR using the OS Module.

        # 2nd Movement - Half Green
        print(f"""{Fore.GREEN}
            ████████ ██  ██████               ████████  █████   ██████               ████████  ██████  ███████ 
               ██    ██ ██                       ██    ██   ██ ██                       ██    ██    ██ ██      
               ██    ██ ██          █████        ██    ███████ ██          █████        ██    ██    ██ █████ {Style.RESET_ALL}{Fore.BLUE}  
               ██    ██ ██                       ██    ██   ██ ██                       ██    ██    ██ ██    
               ██    ██  ██████                  ██    ██   ██  ██████                  ██     ██████  ███████ 
                                                                                                               {Style.RESET_ALL}
            """)
        time.sleep(0.3)                                 # Sleeps for 1/3rd of a second.
        os.system('clear')                              # Expecting a Linux System. Performs a CLEAR using the OS Module.

        # 3rd Movement - All Green
        print(f"""{Fore.GREEN}
            ████████ ██  ██████               ████████  █████   ██████               ████████  ██████  ███████ 
               ██    ██ ██                       ██    ██   ██ ██                       ██    ██    ██ ██      
               ██    ██ ██          █████        ██    ███████ ██          █████        ██    ██    ██ █████ 
               ██    ██ ██                       ██    ██   ██ ██                       ██    ██    ██ ██      
               ██    ██  ██████                  ██    ██   ██  ██████                  ██     ██████  ███████ 
                                                                                                               {Style.RESET_ALL}
            """)
        time.sleep(0.5)                                 # Sleeps for 1/2  of a second. The long delay here is for the animation loop to sink in.
        count = count + 1                               # Increments the loop.
        return(count)                                   # Returns count outside of the function.

    def pregame_loop(count):
        while True:
            try:
                if ascii_animation(count) < 1:              # HELP: <1 loops through twice. <2 loops through 4 times. Supposed to Loops through the ascii_animation function 3 times.
                    count = ascii_animation(count) + 1  # Updates the count variable from what was given by the ascii_animation function.
                    pass
                else:                                       # Upon a success, print the game screen one last time to illustrate the last state of the animation and additionally present the "Press any key" dialogue to prompt the user to proceed.
                    os.system('clear')                      # Expecting a Linux System. Performs a CLEAR using the OS Module.
                    key_press = input(str(f"""{Fore.GREEN}
            ████████ ██  ██████               ████████  █████   ██████               ████████  ██████  ███████ 
               ██    ██ ██                       ██    ██   ██ ██                       ██    ██    ██ ██      
               ██    ██ ██          █████        ██    ███████ ██          █████        ██    ██    ██ █████ 
               ██    ██ ██                       ██    ██   ██ ██                       ██    ██    ██ ██      
               ██    ██  ██████                  ██    ██   ██  ██████                  ██     ██████  ███████ 
                                                                                                               {Style.RESET_ALL}
                    Press any key (then ENTER) to start. Press Enter to replay the Animation: """))
                    if key_press != "":                         # Checks for non-characters.
                        os.system('clear')                      # Expecting a Linux System. Performs a CLEAR using the OS Module.
                        break
                    else:
                        os.system('clear')                      # Expecting a Linux System. Performs a CLEAR using the OS Module.
                        #print(f"\t\t\t {Fore.RED} Follow instructions or type CTRL+C to quit. {Style.RESET_ALL}\n")
                        pass
            except KeyboardInterrupt:                   # Triggers on Keyboard Interrupt (^C) / (CTRL+C)
                print(f"{Fore.RED}\nInterrupted by User{Style.RESET_ALL}")
                os.sys.exit()

    def pregame_rules():
        while True:                                     # https://stackoverflow.com/questions/2244270/get-a-try-statement-to-loop-around-until-correct-value-obtained
            try:                                        # An attempt at catching errors and forcing data types on input.
                print(f"The rules are simple. \n\t1. There are 2 players. \n\t2. The first player selected will be 'x' and will go first. \n\t3. The second player will be 'o' and goes second. \n\t4. To WIN: Vertically, horizontally or diagnoally get 3 of your symbols in a row on the grid. \n\t5. A TIE occurs in which neither player gets 3 symbols in a row.\n")
                key_press = input(str(f"If you accept the rules, press any key (then ENTER) to start the game: "))
                if key_press != "":                         # Checks for non-characters.
                    os.system('clear')                      # Expecting a Linux System. Performs a CLEAR using the OS Module.
                    break
                else:
                    os.system('clear')                      # Expecting a Linux System. Performs a CLEAR using the OS Module.
                    print(f"\t\t\t {Fore.RED} Follow instructions or type CTRL+C to quit. {Style.RESET_ALL}\n")
                    pass
            except KeyboardInterrupt:                   # Triggers on Keyboard Interrupt (^C) / (CTRL+C)
                print(f"{Fore.RED}\nInterrupted by User{Style.RESET_ALL}")
                os.sys.exit()

    # Calls "pregame()" subfunctions
    ascii_animation(count)
    pregame_loop(count)
    pregame_rules()

def game(winner):
    win = False                                         # Keeps track of WIN state. Starts off False because no one has won yet!
    winner = ""
    # Establish a dictionary to hold the values. We will reference the keys for the board position & replace the values with the player's markers (x or o).
    game_state_dict = {
    "1": "1", "2": "2", "3": "3",
    "4": "4", "5": "5", "6": "6",
    "7": "7", "8": "8", "9": "9"}

    def game_call_gamestate(game_state_dict):
        #This prints the values from 'game_state_dict' (if the key is '1', then it'll print the value 1). When a player chooses value '1' as their coordinate, it'll be overwritten with their maker (x or o). This will let us dynmically update the board state throughout the game. Player chooses their value through the player1/2 input functions.
        board = print(f"""
    \t {game_state_dict['1']} | {game_state_dict['2']} | {game_state_dict['3']} 
    \t___|___|___
    \t   |   |   
    \t {game_state_dict['4']} | {game_state_dict['5']} | {game_state_dict['6']} 
    \t___|___|___
    \t   |   |   
    \t {game_state_dict['7']} | {game_state_dict['8']} | {game_state_dict['9']} \n""")

    def game_player1_input():
        nonlocal win                                    # CRITICAL: Used for expanding variable scope through nested functions.
        game_call_gamestate(game_state_dict)            # Call the board gamestate within each player's turn so it can be drawn for each move.
        while True:                                     # https://stackoverflow.com/questions/2244270/get-a-try-statement-to-loop-around-until-correct-value-obtained
            try:                                        # An attempt at catching errors and forcing data types on input.
                p1 = input(f"Player 1 ({Fore.CYAN}x{Style.RESET_ALL}), where would you like to place your symbol in (1-9)?: ")   # Player 1 submits input.
                if p1 in ('1','2','3','4','5','6','7','8','9'):
                    break
                else:                                   # Triggers on int input that is not 1,2,3,4,5,6,7,8,9.
                    print(f"{Fore.RED}Your input is supposed to be an integer between 1-9!!{Style.RESET_ALL}")
                    pass
            except KeyboardInterrupt:                   # Triggers on Keyboard Interrupt (^C) / (CTRL+C)
                print(f"{Fore.RED}\nInterrupted by User{Style.RESET_ALL}")
                os.sys.exit()                           # https://docs.python.org/3/library/os.html
        game_state_dict[p1] = 'x'                       # Assigns the value of the player's selection to their maker.
        os.system('clear')                              # Expecting a Linux System. Performs a CLEAR using the OS Module.
        win_state = win_check_x(game_state_dict)        # Check for win state based off the win_check_x function. The function returns "win = 'True' or 'False'". It will populate the variable 'win' with the value.
        win = win_state
        if win == True:
            nonlocal winner 
            winner = "Player 1"
            return(win, winner)

    def game_player2_input():
        nonlocal win                                    # CRITICAL: Used for expanding variable scope through nested functions.
        game_call_gamestate(game_state_dict)            # Call the board gamestate within each player's turn so it can be drawn for each move.
        while True:                                     # https://stackoverflow.com/questions/2244270/get-a-try-statement-to-loop-around-until-correct-value-obtained
            try:                                        # An attempt at catching errors and forcing data types on input.
                p2 = input(f"Player 2 ({Fore.CYAN}o{Style.RESET_ALL}), where would you like to place your symbol in (1-9)?: ")   # Player 1 submits input.
                if p2 in ('1','2','3','4','5','6','7','8','9'):
                    break
                else:                                   # Triggers on int input that is not 1,2,3,4,5,6,7,8,9.
                    print(f"{Fore.RED}Your input is supposed to be an integer between 1-9!!{Style.RESET_ALL}")
                    pass
            except KeyboardInterrupt:                   # Triggers on Keyboard Interrupt (^C) / (CTRL+C)
                print(f"{Fore.RED}\nInterrupted by User{Style.RESET_ALL}")
                os.sys.exit()   
        game_state_dict[p2] = 'o'                       # Assigns the value of the player's selection to their maker.
        os.system('clear')                              # Expecting a Linux System. Performs a CLEAR using the OS Module.
        win_state = win_check_o(game_state_dict)          # Check for win state based off the win_check_x function. The function returns "win = 'True' or 'False'". It will populate the variable 'win' with the value.
        win = win_state
        if win == True:
            nonlocal winner 
            winner = "Player 2"
            return(win, winner)

    # Calls 'game()' subfunctions
    while win == False:
        game_player1_input()
        if win == True:
            return(winner)
        game_player2_input()
        if win == True:
            return(winner)

def win_check_x(game_state_dict):                       # Checks win condition based off dictionary values containing the string 'x'.
    x = "x"                                             # This is pretty redundant. I could evlatuate on the next line down "if dict["1"] == 'x' (the literal 'x' string) instead of having the program say x = 'x', so make sure dict["1"] == x, but this whole block was made separately."
    if game_state_dict["1"] == x and game_state_dict["2"] == x and game_state_dict["3"] == x:   # X: TRUE: ROW: 123
        win = True; return(win)
    elif game_state_dict["4"] == x and game_state_dict["5"] == x and game_state_dict["6"] == x: # X: TRUE: ROW: 456
        win = True; return(win)
    elif game_state_dict["7"] == x and game_state_dict["8"] == x and game_state_dict["9"] == x: # X: TRUE: ROW: 789
        win = True; return(win)
    elif game_state_dict["1"] == x and game_state_dict["4"] == x and game_state_dict["7"] == x: # X: TRUE: COL: 147
        win = True; return(win)
    elif game_state_dict["2"] == x and game_state_dict["5"] == x and game_state_dict["8"] == x: # X: TRUE: COL: 258
        win = True; return(win)
    elif game_state_dict["3"] == x and game_state_dict["6"] == x and game_state_dict["9"] == x: # X: TRUE: COL: 369
        win = True; return(win)
    elif game_state_dict["1"] == x and game_state_dict["5"] == x and game_state_dict["9"] == x: # X: TRUE: DIAG: 159
        win = True; return(win)
    elif game_state_dict["3"] == x and game_state_dict["5"] == x and game_state_dict["7"] == x: # X: TRUE: DIAG: 357
        win = True; return(win)
    else:
        win = False; return(win)

def win_check_o(game_state_dict):                       # Checks win condition based off dictionary values containing the string 'o'.
    o = 'o'
    if game_state_dict["1"] == o and game_state_dict["2"] == o and game_state_dict["3"] == o:   # O: TRUE: ROW: 123
        win = True; return(win)
    elif game_state_dict["4"] == o and game_state_dict["5"] == o and game_state_dict["6"] == o: # O: TRUE: ROW: 456
        win = True; return(win)
    elif game_state_dict["7"] == o and game_state_dict["8"] == o and game_state_dict["9"] == o: # O: TRUE: ROW: 456
        win = True; return(win)
    elif game_state_dict["1"] == o and game_state_dict["4"] == o and game_state_dict["7"] == o: # O: TRUE: ROW: 789
        win = True; return(win)
    elif game_state_dict["2"] == o and game_state_dict["5"] == o and game_state_dict["8"] == o: # O: TRUE: COL: 147
        win = True; return(win)
    elif game_state_dict["3"] == o and game_state_dict["6"] == o and game_state_dict["9"] == o: # O: TRUE: COL: 369
        win = True; return(win)
    elif game_state_dict["1"] == o and game_state_dict["5"] == o and game_state_dict["9"] == o: # O: TRUE: DIAG: 159
        win = True; return(win)
    elif game_state_dict["3"] == o and game_state_dict["5"] == o and game_state_dict["7"] == o: # O: TRUE: DIAG: 357
        win = True; return(win)
    else:
        win = False; return(win)

def endgame(winner):
    print(f"\nCongratulations!{Fore.GREEN}\n{winner}{Style.RESET_ALL} is the winner!")

def main():
    winner = ""
    pregame()
    winner = game(winner)
    endgame(winner)

main() 
