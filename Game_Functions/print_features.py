def print_guessed(secret_word, letters_guessed):
    '''
    Prints a string that contains the word with a dash "-" in
    place of letters not guessed yet. 
    '''
    
    word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word += letter
        else:
            word += "_ "
    print("Your guess ", word)
    print_line_separator()
    return word

def print_line_separator():
    """ Used as a separator for clarity in the game"""
    return print("--------------")