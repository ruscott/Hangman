def match_with_gaps(letters_guessed, word, other_word):
    """
    A function to match two words together when there are still unknown letters. 
    This excludes words with letters that have already been guessed yet 
    """
    word = word.replace(" ", "")
    if len(word) != len(other_word):
        return False

    for i in range(0,len(word)):
        if word[i] == "_":
            if other_word[i] in letters_guessed:
                return False
            else:
                next
        elif word[i] == other_word[i]:
            next
        else:
            return False

    return True

def show_possible_matches(words_dict, letters_guessed, word):
    """
    Returns all words that are matched with the current hangman
    """
    for possible_word in words_dict:
        if match_with_gaps(letters_guessed, word, possible_word):
            print(possible_word)
        else:
            next
    return