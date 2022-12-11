from random import randrange

def get_word(words_dict):
    '''
    Get random word from dictionary
    '''
    word=words_dict[randrange(0, len(words_dict))]
    return word

def load_words(filename):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(filename)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    print("Enter play_hangman() to play a game of hangman!")
    return wordlist