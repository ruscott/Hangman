from Game_Functions.end_game import end_game

def guesses_update(guesses_left, n = 1):
    """ 
    Update number of guesses left, specify how many guesses lose with the default as 1
    """
    guesses_left = guesses_left - n

    if guesses_left <= 0:
        end_game()
    else:
        print("You have ", guesses_left, "guesses left")
        return guesses_left


def warning_update(warnings_left, guesses_left):
    """ 
    Update number of warnings left, a warning is handed out for wrong character inputs
    """

    warnings_left -= 1
    if warnings_left <= 0:
        print("No more warnings")
        guesses_left = guesses_update(guesses_left)
        return warnings_left, guesses_left
    else:
        print(f"You have {warnings_left} warnings left")
        return warnings_left, guesses_left