# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    output = ""
    
    for letter in secret_word:
        if letter in letters_guessed: 
            output += letter
        else: 
            output += "_ "
    return output 




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = ""
    
    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters += letter 
    
    return available_letters
    

def countUniqueChar(secret_word):
    count = 0
    tracker = ""
    
    for letter in secret_word:
        if letter not in tracker:
            tracker += letter
            count += 1
            
    return count

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    secret_word_length = len(secret_word)
    guesses = 6
    letters_guessed = []
    i = 0
    warnings_remaining = 3
    vowels = ['a','e','i','o','u']
    
    # Start game
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {secret_word_length} letters long.")
    print(f"You have {warnings_remaining} warnings left.")
    
    while True: 
        print("-------------")
        print(f"You have {guesses} guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))
        
        user_input = input("Please guess a letter:")
        # If user inputs an alphabet...
        if (user_input.isalpha()) == True:
            # If user already has guessed that letter...
            if (user_input.lower()) in letters_guessed:
                # User loses a guess if they have 0 warnings left
                if warnings_remaining == 0:
                    guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess " + get_guessed_word(secret_word, letters_guessed))
                # User loses a warning if they still have warnings
                else:
                    warnings_remaining -= 1
                    print(f"Oops! You've already guessed that letter. You now have {warnings_remaining} warnings: " + get_guessed_word(secret_word, letters_guessed))
            # If user hasn't guessed the letter yet, add to letters_guessed list
            else: 
                letters_guessed.append(user_input.lower())
                
                if letters_guessed[i] in secret_word:
                    print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                else:
                    print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                    # If user guessed a vowel that isn't in the secret word, lose 2 guesses.
                    if letters_guessed[i] in vowels:
                        guesses -= 2
                    else: 
                        guesses -= 1
                i += 1 
                        
        # If user inputs anything besides an alphabet...
        else:
            # User loses a guess if they have 0 warnings left
            if warnings_remaining == 0:
                    guesses -= 1
                    print("Oops! That is not a valid letter. You have no warnings left so you lose one guess " + get_guessed_word(secret_word, letters_guessed))
            # User loses a warning if they still have warnings
            else:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: " + get_guessed_word(secret_word, letters_guessed))
                
        
        # If user runs out of guesses, end the game and reveal the secret word.
        if guesses <= 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break 
        
        # Check if the secret word has been guessed
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("Congratulations, you won!") 
            print(f"Your total score for this game is: {guesses * countUniqueChar(secret_word)}")
            break
        



        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # Remove spaces in the word
    my_word_nospace = my_word.replace(" ","")
    
    # Check if the length of my_word = length of other_word
    if len(my_word_nospace) != len(other_word):
        return False
    
    for i in range(len(my_word_nospace)):
        # Check if the i-th letter in my_word and other_word are the same
        if my_word_nospace[i] == other_word[i]:
            continue 
        # Check that the hidden letter "_" hasn't already been revealed in the word
        elif my_word_nospace[i] == "_":
            if other_word[i] in my_word_nospace:
                return False
        else:
            return False
    
    return True

# print(match_with_gaps("t_ _ t", "tarp"))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            matches.append(word)
    
    if len(matches) > 0:
        # print(matches)
        print("Possible word matches are: " + ' '.join(matches))
    else:
        print("No matches found")
            
# show_possible_matches("t_ _ t")
# show_possible_matches("abbbb_ ")
# show_possible_matches("a_ pl_ ")

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    secret_word_length = len(secret_word)
    guesses = 6
    letters_guessed = []
    i = 0
    warnings_remaining = 3
    vowels = ['a','e','i','o','u']
    
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {secret_word_length} letters long.")
    print(f"You have {warnings_remaining} warnings left.")
    
    while True: 
        print("-------------")
        print(f"You have {guesses} guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))
        
        user_input = input("Please guess a letter:")
        
        # If user inputs an alphabet...
        if (user_input.isalpha()) == True:
            # If user already has guessed that letter...
            if (user_input.lower()) in letters_guessed:
                # User loses a guess if they have 0 warnings left
                if warnings_remaining == 0:
                    guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess " + get_guessed_word(secret_word, letters_guessed))
                # User loses a warning if they still have warnings
                else:
                    warnings_remaining -= 1
                    print(f"Oops! You've already guessed that letter. You now have {warnings_remaining} warnings: " + get_guessed_word(secret_word, letters_guessed))
            # If user hasn't guessed the letter yet, add to letters_guessed list
            else: 
                letters_guessed.append(user_input.lower())
                
                if letters_guessed[i] in secret_word:
                    print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                else:
                    print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                    # If user guessed a vowel that isn't in the secret word, lose 2 guesses.
                    if letters_guessed[i] in vowels:
                        guesses -= 2
                    else: 
                        guesses -= 1
                i += 1 
                
        # If user inputs an asterisk *...
        elif user_input == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        
        # If user inputs anything besides an alphabet...
        else:
            # User loses a guess if they have 0 warnings left
            if warnings_remaining == 0:
                    guesses -= 1
                    print("Oops! That is not a valid letter. You have no warnings left so you lose one guess " + get_guessed_word(secret_word, letters_guessed))
            # User loses a warning if they still have warnings
            else:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: " + get_guessed_word(secret_word, letters_guessed))
                
        
        # If user runs out of guesses, end the game and reveal the secret word.
        if guesses <= 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break 
        
        # Check if the secret word has been guessed
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("Congratulations, you won!") 
            print(f"Your total score for this game is: {guesses * countUniqueChar(secret_word)}")
            break


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    secret_word = "apple"
    hangman_with_hints(secret_word)
