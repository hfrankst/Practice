"""
a number guessing game
"""

import random

def game():
    
    #generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    #limit guesses    
    while len(guesses) < 5:
        #get a number guess from the player
        try:
            #safely make an int
            #important to do this because it is converting the type of the object and could backfire
            guess = int(input("Guess a number between 1 and 10: "))
        #catch if user doesn't enter a number
        except ValueError:
            print('{} is not a number. Enter a number'.format(guess))
        else:           
            
            #compare guess to secret answer
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print('{} is too Low!'.format(guess))            
            #print hit/miss
            else:
                print("{} is too high.".format(guess))
            guesses.append(guess)
    else:
        print("You didn't get it! My number was {}.".format(secret_num))

    #play again
    play_again = input('Do you want to play again? Y/n')
    if play_again.lower() != 'n':
        game()
        
game()