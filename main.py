from os import system
from datetime import datetime as dt
from morse import morse_codes, logo4

FILENAME = "converted_messages.txt"


def to_morse_code():
    # Get message from user
    message = input("Enter message to convert to Morse Code: \n").upper()
    # Create a list for the characters
    morse_list = []
    # Go through the string of characters in message and substitute the corresponding morse code
    for char in message:
        if char == " ":
            morse_list.append(" ")
        else:
            try:
                morse_list.append(morse_codes[char] + " ")
            except KeyError:
                # if character entered is not part of morse code, add a space instead
                morse_list.append(" ")

    # Create a string from the list of symbols
    morse_message = "".join(morse_list)
    print(f"Your converted message:\n{morse_message}")
    # Print the message and converted code to a file
    with open(FILENAME, "a") as file_output:
        time = str(dt.now())
        file_output.write(f"{time[:-7]} : {message} >> {morse_message}\n\n")

    again = input("Would you like to convert another message to Morse Code? Y/N ").upper()
    if again == "Y":
        to_morse_code()


def to_plain_text():
    encoded_message = input("Enter message to convert from Morse Code (Use single space between characters,"
                            " 2 spaces between words): \n")

    # Function to get the letter from morse code dictionary
    def get_letter(val: str):
        for key, value in morse_codes.items():
            if val == value:
                return key
        return "invalid"
        # returns invalid if the letter was not found in the dictionary

    # Keep track of how many spaces between symbols
    space = 0
    # Add space to end of message to get last character
    encoded_message += ' '
    plain_list = []
    current_character = ''
    # Go through each symbol and check for character or spaces
    for symbol in encoded_message:
        # Build each character with symbols until space detected
        if symbol != ' ':
            space = 0
            current_character += symbol
        else:
            space += 1
            # New word, so add a space
            if space == 2:
                plain_list.append(" ")
            else:
                # 1 space detected, so look up completed character in dictionary
                letter = get_letter(current_character)
                if letter != "invalid":
                    plain_list.append(letter)
                # reset current character
                current_character = ''
    if plain_list:
        # Create a string from the list of characters
        plain_message = "".join(plain_list)
        print(f"Your converted message:\n{plain_message}")
        # Print the code and converted text to a file
        with open(FILENAME, "a") as file_output:
            time = str(dt.now())
            file_output.write(f"{time[:-7]} : {encoded_message} >> {plain_message}\n\n")
    else:
        print("Invalid morse code. Please try again.")

    again = input("Would you like to convert another message from Morse Code? Y/N ").upper()
    if again == "Y":
        to_plain_text()


def ask_direction():
    system("clear")
    print(logo4)
    return input("Would you like to convert TO or FROM Morse Code? T/F (Type 'E' to Exit) ").upper()


program_active = True
while program_active:

    # Check if encoding to or decoding from Morse
    answer = ask_direction()
    if answer == "T":
        to_morse_code()

    elif answer == "F":
        to_plain_text()

    elif answer == "E":
        # End program
        program_active = False
        print(f"Your converted messages have been added to {FILENAME}.\n Goodbye.")
