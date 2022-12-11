from string import *
from Game_Functions.print_features import print_guessed
from Game_Functions.guess_update import guesses_update
import Game_Functions.end_game as end_game

def letter_correct(guess, secret_word):
    """
    This function checks if a letter is in a word. This returns true when the letter is in the word, and false when it isn't
    """
    if guess in secret_word:
        return True
    else: return False

def result_from_letter(is_vowel, guesses_left, secret_word, letters_guessed):
    """
    Checks if letter is in secret word and updates the guesses accordingly
    """
    print_guessed(secret_word, letters_guessed)
    if is_vowel:
        guesses_left = guesses_update(guesses_left, 2)
    else:
        guesses_left = guesses_update(guesses_left)
    get_available_letters(letters_guessed)
    return guesses_left

def return_letter_is_in_word(secret_word, letters_guessed, guesses_left):
    """ 
    A function that updates guesses when letter is in the word
    """

    print("Letter in word!")
    word = print_guessed(secret_word, letters_guessed)
    print(f"You have {guesses_left} guesses left")
    if end_game.is_word_guessed(secret_word, letters_guessed):
        print("Well done you have successfully guessed the word!")
        end_game.tot_score(guesses_left, secret_word)
        return end_game.play_again()
    get_available_letters(letters_guessed)
    return word, guesses_left

def return_letter_not_in_word(letter, guesses_left, secret_word, letters_guessed):

    """ 
    A function that updates guesses when letter is not in the word
    """

    vowels = ["a", "e", "i", "o", "u"]

    is_vowel = letter in vowels
    print("Letter not in word")
    if is_vowel:
        print("Vowel used, lose two guesses")
    guesses_left = result_from_letter(is_vowel, guesses_left, secret_word, letters_guessed)
    return guesses_left

def get_available_letters(letters_guessed):
    """ 
    Returns letters that haven't been used yet from the alphabet.
    """    
    letters_left = ascii_lowercase

    for letter in letters_guessed:
        if letter in letters_left:
            letters_left = letters_left.replace(letter, "")
    print("Letters still available to use ", letters_left)