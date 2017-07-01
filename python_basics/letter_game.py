"""
a letter guessing game
"""



import random
import os




#make a list of words
words = [
    'apple',
    'strawberry',
    'raspberry',
    'pear',
    'blackberry',
    'banana',
    'watermelon',
    'kumquat',
    'plum',
    'star fruit',
    'peach',
    'orange',
    'grapefruit',
    'blueberry'
]


# a method to clear the cli
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# a method to handle the user's guesses
def draw(bad_guesses, good_guesses, secret_word):
    clear()
    
    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')
    
    for letter in bad_guesses:
        print(letter, end='')
    print('\n\n')
    
    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else: 
            print('_', end='')
    print('')
 
# a method to evaluate the guess against the 'secret word'
def get_guess(bad_guesses, good_guesses):
    #take guess
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print('You can only guess a single letter!')
        continue
    elif guess in bad_guesses or guess in good_guesses:
        print("You've already guesses that letter.")
        continue
    elif not guess.isalpha():
        print("You can only guess letters!")
        continue

while True:
    start = input('Press Enter or Return to start, or enter Q to quit')
    if start.lower() == 'q':
        break
    
    #pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
    
    # this while loop limits the number of guesses a user can make
    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        
        #draw guessed letters and strikes
        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You Win! The word was {}.".format(secret_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("You didn't guess it! The word was {}.".format(secret_word))
   
