
# Written by David Blum April 1st, 2016
# Project: Fill in the Blank
# IPND Stage 2 Final Project

# Sets up paragraphs and answers for different difficulty levels
easy_ans = ['Python', 'language', 'variables', 'declare']
easy_para = '''__1__, similar to C++ and Java, is a __2__ programmers use to write programs.
Every __2__ is slightly different and uses different syntax. In __1__ assigning
__3__ is as simple as "a='hello'". Unlike other __2__s you do not need to __4__
__3__ in __1__.'''


med_ans = ['int', 'float', '3.5', 'immutable']
med_para = '''Python has two different types of numbers: __1__ and __2__. In computing values,
Python will only return __1__ if all numbers are an __1__; otherwise it will return a __2__.
i.e. "7/2" returns "3" whereas "7.0 / 2" returns "__3__".

In Python strings are __4__, they cannot be changed. Numbers, lists, and dictionaries are not __4__.'''

hard_ans = ['loops','elements','debugging','traceback','comments']
hard_para = '''Two common __1__ in python are "for" and "while". "For" __1__ are good at going
through a static index of __2__, whereas "while" __1__ are useful for when the number
of __2__ is unknown.

Bugs happen. The process of getting rid of bugs in programs is called __3__. After
running the program in the console, the __4__ will display any errors in your code.

Use of __5__ helps to avoid bugs and makes it easier for others to understand your code.'''


def user_choice(choices, question):
    """user_choice(list, string): CHOICES list is list of acceptable user input.
    QUESTION string prompts user with a question. Returns user-string in UPPERCASE."""
    choice = None
    while choice not in choices:
        choice = raw_input("\n" + question + "\n").upper()
    return choice

'''
# Outdated code. Chose to replace with user_choice. Originally returned ANY positive, whole number.
# Large, positive numbers run outside scope of game
def lives():
    """lives(): prompts user and returns a positive, whole number."""
    hearts = 'empty'
    #checks input for positive, whole numbers
    while not hearts.isdigit() or int(hearts) == 0:
            hearts = raw_input("\nHow many attempts per word? (Pick a positive, whole number) \n")
    return int(hearts)
'''

def user_guess(target, answer, guesses):
    """"user_guess(string, string, int): TARGET string is what blank the user is
    attemtping to fill in. ANSWER string is the correct answer for the blank.
    GUESSES int is number of guesses allowed. Returns TRUE if guess is correct,
    FALSE if user runs out of guesses"""
    for current_guess in range(guesses):
        # provides a hint on last guess if guesses > 1
        if guesses > 1 and current_guess == guesses - 1:
            print "Hint: " + answer[0] + "_" * (len(answer[1:-1])) + answer[-1]
        # prompts user input
        user_input = raw_input("\n\nWhat should be substituted for " + target + "?\n").upper()
        # if user guesses correctly return TRUE
        if user_input == answer.upper():
            print "You are correct!"
            return True
        # Otherwise lower the amount of guesses_left
        guesses_left = guesses-(current_guess+1)
        if guesses_left == 1:
            print "You have " + str(guesses_left)  + " guess left"
        else:
            print "You have " + str(guesses_left)  + " guesses left"
    # User ran out of guesses, returns FALSE
    return False

def level(stage, guesses):
    """level(string, int): Loads level. STAGE string is the KEY from dif_levels
    dictionary with the value of the level's paragraph and it's answers. GUESSES int
    is the number of allowed guesses per blank. Updates paragraph until user runs out
    of guesses or guesses every word. PRINT end game condition and RETURNS to exit level"""
    num_answers = len(stage[1])
    current_word = 1
    # While there are answers and guesses left...
    while current_word <= num_answers and guesses > 0:
        answer = stage[1][current_word-1]
        target = "__" + str(current_word) + "__"
        print "\n\nThe current paragraph reads: \n\n" + stage[0]
        # If user runs out of guesses
        if user_guess(target, answer, guesses) == False:
            print "\nYou LOSE"  
            return 
        # If guess is correct updates paragraph
        stage[0] = stage[0].replace(target, answer)
        current_word += 1
    # If user guess every word correctly
    print "\n" + stage[0] + "\n\nYou Win!"
    return

def game_on():
    """game_on(): No Input. Runs until user chooses not to play again."""
    playing = True
    while playing:
        # Being inside loop allows levels to reset upon multiple playthoughs
        dif_levels = {"EASY": [easy_para, easy_ans],
               "MEDIUM": [med_para, med_ans],
               "HARD": [hard_para, hard_ans]}
        
        # Title
        print "\n\n     FILL IN THE BLANKS \n"

        # Prompts User for settings
        difficulty = user_choice(dif_levels.keys(), "Choose a difficulty: EASY, MEDIUM, HARD")
        attempts = user_choice(['1','2','3'], "How many attempts per word? 1, 2, or 3?")

        # Runs level based on user settings
        level(dif_levels[difficulty], int(attempts))

        # Play again?
        again = user_choice (['YES', 'Y', 'NO', 'N'], "Would you like to play again? Y/N") 
        if again == 'NO' or again == 'N':
            print "\nThanks for Playing!"
            playing = False
        
# Command to run FILL IN THE BLANK game
game_on()


