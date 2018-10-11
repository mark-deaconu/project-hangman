
def main():
    show_title_screen()
    secret_word = get_secret_word()
    correct_guesses = ""
    wrong_guesses = ""

    while (not word_is_solved(secret_word, correct_guesses) and
            not player_is_dead(wrong_guesses)):
        display_platform(wrong_guesses)
        display_letters(secret_word, correct_guesses)
        guess = get_guess()

        # HANDLE GUESS
        # if guess is in the word, the add it to the correct guesses
        # otherwise, add it to the incorrect guesses

    if word_solved(secret_word, correct_guesses):
        show_win_screen()
    else:
        show_lose_screen()


def get_secret_word():
    """Will return a single word from a list of words.
    
    Returns:
        Single word from a list
    """
    import random
    word_bank = [
        "Dog", "Matcha", "Brain", "Brother", "Player", "Cerebrum",
        "Trachea", "Fiblia", "Construct", "Construction", "Cell",
        "Mitochondria", "Power", "Calcium"
    ]
    return random.choice(word_bank)


def word_is_solved(word, guesses):
    """Will check to see if a word has been completely solved.
    
    Args:
        word (str): The secret word
        guesses (str): The string containing all correct guesses
        
    Returns:
        bool: True if word is solved, False if word is not.
    """
    pass

    return set(word.replace(' ', '')) <= set(guesses)


def player_is_dead(wrong_guesses):
    """Determines if the player is dead (too many guesses).
    
    Args:
        bad_guesses (str): A string containing all of the wrong guesses
        
    Returns
        bool: True if dead, False otherwise
    """
    return len(wrong_guesses) >= 6
 

def display_platform(wrong_guesses):
    """Displays (prints) hanging platform based on how many incorrect guesses.
    
    Args:
        wrong_guesses (str): A string containing all wrong guesses.
    """
    if len(wrong_guesses) == 0:
        print('''
 _____
 |
 |
 |
_|__
''')
    elif len(wrong_guesses) == 1:
        print('''
 _____
 |  Ó
 |
 |
_|__
''')
    elif len(wrong_guesses) == 2:
        print('''
 _____
 |  Ó
 |  |
 |
_|__
''')
    elif len(wrong_guesses) == 3:
        print('''
 _____
 |  Ó
 | /|
 |
_|__
''')
    elif len(wrong_guesses) == 4:
        print('''
 _____
 |  Ó
 | /|\ 
 |
_|__
''')
    elif len(wrong_guesses) == 5:
        print('''
 _____
 |  Ó
 | /|\ 
 | /
_|__
''')
    else:
        print('''
 _____
 |  Ó
 | /|\ 
 | / \ 
_|__
''')
        

def display_letters(word, guesses):
    """Displays (prints) the letter-board,
    underscores (_) for letters not yet guessed.
    
    Args:
        word (str): The secret word
        guesses (str): A string of correct guesses
    """
    pass


def get_guess():
    """Will take the user's guess. Ensures the input is valid."""
    while True:
        letter = input('Enter a letter:').lower()

        if letter.isalpha() and len(letter) == 1:
            return letter

        print('Character is invalid. ',end='')

    
    

def show_title_screen():
    """Will display ASCII art for a title screen"""
    print(" _    _              _   _    _____   __  __              _   _ ")
    print("| |  | |     /\     | \ | |  / ____| |  \/  |     /\     | \ | |")
    print("| |__| |    /  \    |  \| | | |  __  | \  / |    /  \    |  \| |")
    print("|  __  |   / /\ \   | . ` | | | |_ | | |\/| |   / /\ \   | . ` |")
    print("| |  | |  / ____ \  | |\  | | |__| | | |  | |  / ____ \  | |\  |")
    print("|_|  |_| /_/    \_\ |_| \_|  \_____| |_|  |_| /_/    \_\ |_| \_|")

def show_win_screen():
    """Will display ASCII art for a win screen"""
    print("_____.___.                      .__         ._.         ___    ")
    print("\__  |   | ____  __ __  __  _  _|__| ____   | |     /\  \  \   ")
    print(" /   |   |/  _ \|  |  \ \ \/ \/ /  |/    \  | |     \/   \  \  ")
    print(" \____   (  <_> )  |  /  \     /|  |   |  \  \|     /\    )  ) ")
    print(" / ______|\____/|____/    \/\_/ |__|___|  /  __     \/   /  /  ")
    print(" \/                                     \/   \/         /__/   ")


def show_lose_screen():
    """Will display ASCII art for a lose screen"""
    print("_____.___.              .__                        ._.            ___ ")
    print("\__  |   | ____  __ __  |  |   ____  ______ ____   | |     /\    /  / ")
    print(" /   |   |/  _ \|  |  \ |  |  /  _ \/  ___// __ \  | |     \/   /  /  ")
    print(" \____   (  <_> )  |  / |  |_(  <_> )___ \\  ___/   \|      /\  (  (   ")
    print(" / ______|\____/|____/  |____/\____/____  >\___  >  __     \/   \  \  ")
    print(" \/                                     \/     \/   \/           \__\ ")


if __name__ == "__main__":
    main()
