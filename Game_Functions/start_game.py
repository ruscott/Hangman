from string import *
from Game_Functions.print_features import print_line_separator

def play_with_hints():
    hints_input_correct = False
    while not hints_input_correct:
        hints_choice = input("Do you want to play with hints? ")
        if hints_choice in ["Y", "y"]:
            return True
        elif hints_choice in ["N", "n"]:
            return False

def welcome_to_hangman(secret_word, guesses_left):
    """
    A function that returns a welcome to hangman and specifies if the game is being played with hints or not
    """ 

    hints_activated = play_with_hints()
    print(f"Welcome to Hangman!")
    if hints_activated:
        print("You have chosen to play with hints")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print_line_separator()
    print(f"Letters available: {ascii_lowercase}")
    print(f"You have {guesses_left} guesses left")
    return hints_activated