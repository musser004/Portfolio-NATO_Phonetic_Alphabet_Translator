# Simple program to translate a given message into NATO phonetic alphabet names, along with basic punctuation

import pandas

# Reading NATO phonetic alphabet names CSV

dict1 = pandas.read_csv("nato_phonetic_alphabet.csv")

# Setting up new dictionary with keys set to letters and values set to NATO phonetic alphabet names

dict2 = {row.letter:row.code for (index, row) in dict1.iterrows()}

# Manually adding in keys and values for spaces and basic punctuation, to allow for basic user input messages

dict2[" "], dict2["."], dict2["!"], dict2["?"], dict2[","], dict2["'"] = " ", ".", "!", "?", ",", "'"

# Default loop condition

loop_continue = True

# While loop to iterate through the user's input and check dict2 for appropriate name via list comprehension

while loop_continue is True:
    user_reply = (input("Please enter your message (only letters, spaces, and basic punctuation): ").upper())
    user_letters = [x for x in user_reply]

    # Try/except block to deal with KeyError (user entering character not contained within dict2). Otherwise,
    # translated message is printed to terminal

    try:
        nato_letters = [dict2[x] for x in user_letters]
        print(nato_letters)
    except KeyError:
        print("Sorry, only alphabetical letters and spaces, please")
    else:
        loop_continue = False
