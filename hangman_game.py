# Name: Ruchika Scott
# 6.S189 Project 1: Hangman template
# hangman_template.py

# Import functions for game
import Game_Functions.get_word as get_word
import Game_Functions.start_game as start_game
import Game_Functions.end_game as end_game
import Game_Functions.letter_in_word as letter_in_word
from Game_Functions.user_input import letter_input
from Game_Functions.hints_output import show_possible_matches
# -----------------------------------

# CONSTANTS
MAX_GUESSES = 6


WORDLIST_FILENAME = "words.txt"
words_dict = get_word.load_words(WORDLIST_FILENAME)

########
# Play hangman
########

def play_hangman():
    # Actually play the hangman game but with hints included when a * is requested
    #Load in global variables used
    secret_word  = get_word.get_word(words_dict)
    letters_guessed = []
    guesses_left = MAX_GUESSES
    warnings_left = 3
    
    # Welcome to hangman Sequence
    hints_activated = start_game.welcome_to_hangman(secret_word, guesses_left)

    word = "_ " * len(secret_word)
    #Code for hangman
    while not end_game.is_word_guessed(secret_word, letters_guessed) and guesses_left >= 0:
        letter, warnings_left, guesses_left, letters_guessed = letter_input(hints_activated, warnings_left, guesses_left, letters_guessed)
        if letter == "hint":
            print("You have chosen to use a hint!")
            show_possible_matches(letters_guessed, word)
        elif letter_in_word.letter_correct(letter, secret_word):
            word, guesses_left = letter_in_word.return_letter_is_in_word(secret_word, letters_guessed, guesses_left)
        elif not letter_in_word.letter_correct(letter, secret_word):
            guesses_left = letter_in_word.return_letter_not_in_word(letter, guesses_left, secret_word, letters_guessed)
    return 

