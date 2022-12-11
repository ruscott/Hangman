from Game_Functions.print_features import print_line_separator
from Game_Functions.guess_update import warning_update

def input_guess():
    """ 
    This function returns an input letter as a guess
    """
    print_line_separator()
    guess = input("Please input a letter: ")
    #multiple letters take the first with warning
    if len(guess) > 1:
        print("Multiple letters, the guess will be the first letter")
        guess = guess[0]
    else:
        next
    guess = guess.lower()
    return guess

def letter_input(hints_activated, warnings_left, guesses_left, letters_guessed):
    """ 
    Receives a letter guessed from the player, with checks to makes sure its a correct input.
    """
    input_correct = False

    while not input_correct:
        guess = input_guess()

        # When the hint hangman is being played, an extra if statement to return possible available words
        if hints_activated:
            if guess == "*":
                return "hint"
    
        if not str.isalpha(guess):
            print("You have entered an invalid input")
            warnings_left, guesses_left = warning_update(warnings_left, guesses_left)
        elif guess in letters_guessed:
            print("You have already used this letter")
            warnings_left, guesses_left = warning_update(warnings_left, guesses_left)
        else:
            letters_guessed += guess
            return guess, warnings_left, guesses_left, letters_guessed
