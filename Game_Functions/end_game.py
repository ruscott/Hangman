from Game_Functions.print_features import print_line_separator

def end_game(secret_word):    
    print("No more guesses left, you lose!")
    print(f"The word was {secret_word}")
    play_again()

def play_again():
    """
    Play again function to make it easier for person to play again
    """
    print_line_separator()
    play_again = input("Do you want to play again? Y/N: " )
    if play_again == "Y":
        print_line_separator()
        return True
    else:
        return exit()

def tot_score(guesses_left, secret_word):
    """
    This function obtains the score for the hangman game which is the number of guesses left * the number of unique letters in the word
    """

    unique_letters = set(secret_word)
    return print(f"Your score for the game is: {guesses_left * len(unique_letters)}") 


def is_word_guessed(secret_word, letters_guessed):
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    if set(secret_word).issubset(set(letters_guessed)):
        return True
    else: 
        return False

