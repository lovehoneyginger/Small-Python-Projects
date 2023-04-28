import random
import math 
import string


def reading_inputs():
    print('Enter the lower and upper ranges: ')
    a,b = int(input()),int(input())
    return a,b

def check_valid_range(a,b):
    if b-a<3:
        print('\nInvalid range is given')
        print('############################')
        print('Enter valid lower and upper ranges')
        a,b = int(input()),int(input())
        return check_valid_range(a,b)
    elif b-a>=3:
        n = round(math.log(b-a+1,2))
        print('\nYou will have ',n,' guesses')
        print('############################')
        return n
    
def guessing(a,b):
    Number_of_guesses = check_valid_range(a,b)
    Number_to_be_guessed = random.randint(a,b)

    for i in range(Number_of_guesses+1):
        if i < Number_of_guesses:
            print('Enter the guess for guess',i+1)
            guess = int(input())
            if Number_to_be_guessed == guess:
                print('##################################\nSuccess!! You guessed it right\n')
                print('Do you want to continue restart the Guessing Game?')
                answer = input().lower()
                if answer == 'no':
                    exit()
                else:
                    print('#######################################')
                    print('Initiating restart.................')
                    guess_game_main()

            else:
                print('Sorry, You guessed it wrong')
                if Number_to_be_guessed>guess:
                    print('You guessed it lower')
                else:
                    print('#################################')
                    print('You guessed it higher')
                print('Try again!!!')
        else:
            print('You have run out of guesses')
            print('##################################')
            print('Do you want to continue restart the Guessing Game?')
            answer = input().lower()
            if answer == 'no':
                exit()
            else:
                print('#######################################')
                print('Initiating restart.................')
                guess_game_main()

def guess_game_main():
    print('####### The Guessing Game ########\n')
    a,b = reading_inputs()
    guessing(a,b)

guess_game_main()