# Q8
# Expanding on Bobs algorithm assignment.
# Write the game of Hide-and-Seek as an actual Python program.
# You can write it as simply as you want, but it must include the following:
# 1) A few players.
# 2) A count down.
# 3) Some actions for the players.
# Creativity is encouraged!

# Import library
import time
import getpass

# Print out the rules, formatted as table.
def rules():
    print("\n########################################")
    print("######## Welcome to HIDE N SEEK ########")
    print("########################################\n")
    print("The rules are simple. \n\t1. There are 3 players. \n\t2. The players will choose a seeker. \n\t3. The players will choose their hiding spots. \n\t4. The seeker will attempt to find the players. \n\t5. If all players are not found after 4 turns, the players win. Otherwise, if all players are found, the seeker wins.\n")

# Gather User Input
def user_inputs():
#    print("\n\t#### USER INPUTS ####\n")
    player1 = str(input("Player 1, what is your name?: "))
    player2 = str(input("Player 2, what is your name?: "))
    player3 = str(input("Player 3, what is your name?: "))
    timer_value = int(input("How long should the seeker countdown from? (5-30): "))
    return[player1, player2, player3, timer_value] # This is a list.

# Validates player variable input. Not being used at this time. Too complex.
# def input_checks(user_input):

# Seeker Function lets the users select who will seek.
def seeker(user_input):
#    print("\n\t#### SEEKER ####\n")
    # Prints a prompt for the user, referencing index0 (Player1), index1 (Player2) and index2 (Player3).
    print("\nWhich player should be the seeker?\n\t0. " + user_input[0] + "\n\t1. " + user_input[1] + "\n\t2. " + user_input[2])
    # Prompts the user for input, choosing a number selection that corresponds to that index number referenced above.
    seeker_num = int(input("Type in the number (0, 1 or 2) for the seeker: "))
    # References the interger from seeker_num as the index value of user_input (1 = Player2)
    seeker_is = user_input[seeker_num]
    # Prints confirmation of the seeker. This is mostly done for debugging purposes.
    print("The seeker is:", seeker_is)
    # Delete the index number's value of seeker from the list. ie return non-seeker values.
    del user_input[seeker_num]
#    print("This is the new user_input list:", user_input)
    # Until a more elegant solution is devised, also manually delete the last index number value (start_timer) from the list.
    del user_input[-1]
#    print("This is the new user_input list:", user_input)
    hider_list = user_input
    # Return the seeker value to the rest of the program.
    return[seeker_is, hider_list]

# Players choose their hiding spots.
def hiding_spots(hiders):
    # Create Dictionary for hiding spot entries.
    spots = {
            "0" : "Big Tree", 
            "1" : "Big Rock", 
            "2" : "Small Tree", 
            "3" : "Small Rock", 
            "4" : "Big Log", 
            "5" : "Car", 
            "6" : "Up a Tree",
            "7" : "Inside Play Structure",
            "8" : "Inside a Bush",
            "9" : "Cover with Leaves in a gutter"
        }
    
    # Dict used in loop below.
    hiders_dict = {}
    for i in range(0,2):
        # Print out hiding spots for each hider referened by the "hider" arguement value:
        print("\n\n" + hiders[i] + ", where would you like to hide?")
        print("0. " + spots['0'],"\t\t" + "1. " + spots['1'] +"\n"
            "2. " + spots['2'],"\t\t" + "3. " + spots['3'] +"\n"
            "4. " + spots['4'],"\t\t" + "5. " + spots['5'] +"\n"
            "6. " + spots['6'],"\t\t" + "7. " + spots['7'] +"\n"
            "8. " + spots['8'],"\t" + "9. " + spots['9'] +"\n")
        # Asks users for input on where to hide. Getpass hides the printed characters.
        spot_value = getpass.getpass(prompt = "Pick a number 0-9 (input will be hidden): ")
        # This updates the dictionary to house the Hider's hiding spots on each pass of the loop.
        hiders_dict.update({hiders[i]:spot_value})
    return[hiders_dict, spots]

# Validates "start_timer" input.
def timer_checks(start_timer):
#    print("\n\t#### TIMER CHECKS ####\n")
    while True:
        if start_timer in range(5,31):
            break
        else:
            print("Please choose a number between 5 and 30 for the countdown timer.\n")
            continue
    return(start_timer)
        
# Countdown function
def countdown(timer, seeker_be):
#    print("\n\t#### COUNTDOWN ####\n")
    for i in range(timer,0,-1):
        print(str(i))
        time.sleep(.3)
    print("\n" + seeker_be +" says: \"Ready or not, here I come!\"\n")

def seek(seeker, hider_values, hiding_spots):
    # Loops that takes count of turns (t).
    for t in range(4,0,-1):
        print("\n\n" + seeker + ", you have " + str(t) + " turn(s) to find the players!\n")
        print("0. " + hiding_spots['0'],"\t\t" + "1. " + hiding_spots['1'] +"\n"
        "2. " + hiding_spots['2'],"\t\t" + "3. " + hiding_spots['3'] +"\n"
        "4. " + hiding_spots['4'],"\t\t" + "5. " + hiding_spots['5'] +"\n"
        "6. " + hiding_spots['6'],"\t\t" + "7. " + hiding_spots['7'] +"\n"
        "8. " + hiding_spots['8'],"\t" + "9. " + hiding_spots['9'] +"\n")
        seeker_selection = input("Pick a number 0-9: ")
        for hider, value in hider_values.items():
            if seeker_selection == value:
                print("****You found", hider + "!****\n\n")
                hider_values.pop(hider) # Removes found player from list.
                break
            else: 
                print("The seeker didn't find any players this round.")
    return(hider_values)

def endgame(seeker_answer):
    # If the Dict is empty, then players have been found (due to removal from the "hider_values" dict). Otherwise, the player has lost.
    if dict == {}:
        print("\n\nCONGRATULATIONS! YOU WIN! You found all the players! You are the Ultimate Seeker!\n")
    else:
        print("\n\nGAME OVER! YOU Lost! Players still remain!\n")

def main():
    # Print out rules of the game.
    rules()
    
    # Acquire user input.
    user_list = user_inputs()

    # Take index position of user_list function (start_timer) value.
    start_timer = user_list[3]

    # Determine who the seeker will be and who the hiders will be based off user input.
    seeker_be, hider_be = seeker(user_list)

    # Players choose their hiding spots.
    find_players, hiding_values = hiding_spots(hider_be)

    # timer_checks function validates input and hands it off to the countdown function. Passed
    # along seeker_be so the seeker can shout out that they're ready.
    print("\n") # For Formatting
    countdown(timer_checks(start_timer),seeker_be)

    # This function loops through the seeker's answers to try and find the players.
    seeker_answer = seek(seeker_be, find_players, hiding_values)

    # This function displays end game states:
    endgame(seeker_answer)

main()
