# import urllib
# import webbrowser
# def process_user_query(query_string):
#     name_list = query_string.split(' ')
#     greetings = []
#     for name in name_list:
#         if (name[0].isupper()==True):
#             greetings.append(f'Hi {name}!\n')
#     return greetings
#     return 'No names found'
# url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
# webbrowser.open_new(url)

import random

def main():
    welcome = ['Welcome to Hangman! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!'
               ]



    # setting up the play_again loop

    play_again = True

    while play_again:
        # set up the game loop

        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None # will hold the players guess
        guessed_letters = [] # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
        joined_word = None # joins the words in the list word_guessed

        HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  | |
|
--------
""")

        return HANGMAN[0]
        attempts = len(HANGMAN) - 1


        while (attempts != 0 and "-" in word_guessed):
            return(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            return(joined_word)

            try:
                player_guess = str(query_string("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except: # check valid input
                return("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess.isalpha(): # check the input is a letter. Also checks an input has been made.
                    return("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1: # check the input is only one letter
                    return("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters: # check it letter hasn't been guessed already
                    return("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

            if player_guess not in chosen_word:
                attempts -= 1
                return(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed: # no blanks remaining
            return(("\nCongratulations! {} was the word").format(chosen_word))
        else: # loop must have ended because attempts reached 0
            return(("\nUnlucky! The word was {}.").format(chosen_word))

        return("\nWould you like to play again?")

        response = query_string("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()
