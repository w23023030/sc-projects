"""
File: hangman.py
Name: Jasmine Tsai
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    TODO:
    The program will randomly select an English word (represented by answer) from the font library,
    and cover each letter with a dash. Each time the player enters an uppercase or lowercase letter (represented by
    input_ch), if input_ch exists in answer, the program will update the dashes and display all the positions
    of input_ch. However, if input_ch does not exist in answer, the player will lose a life.
    If seven times have not been guessed, seven lives are gone, and the player challenge fails.
    """
    answer = random_word()
    old_word = dashed(answer)
    new_word = old_word
    lives = N_TURNS
    print(old_word)
    print('You have '+str(lives)+' guesses left.')
    while True:
        if lives != 1:
            input_ch = input('Your guess: ')
            input_ch = input_ch.upper()
            size = len(input_ch)
            if input_ch.isalpha() and size < 2:
                if input_ch in answer:
                    # User guessed right.
                    print('You are correct!')
                    if new_word != answer:
                        ans = ''
                        for i in range(len(answer)):
                            ch = new_word[i]
                            if answer[i] == input_ch:
                                ans += input_ch
                            else:
                                ans += ch
                        new_word = ans
                        if new_word == answer:
                            # Guessed it all! End the game.
                            print('You win!!')
                            break
                        else:
                            print('The word looks like: ', end='')
                            print(new_word)
                            print('You have ' + str(lives) + ' guesses left.')

                else:
                    # User guessed wrong.
                    old_word = new_word
                    if lives != 1:
                        print('There is no '+input_ch+'\'s in the word.')
                        print('The word looks like: ', end='')
                        print(old_word)
                        print('You have ' + str(lives - 1) + ' guesses left.')
                    lives -= 1
            else:
                # The format is wrong when the user input is not an English letter or more than one letter.
                print('illegal format.')

        else:
            # The user still guessed wrong when the last time.
            # Guess wrong 7 times and end the game.
            input_ch = input('Your guess: ')
            input_ch = input_ch.upper()
            print('There is no ' + input_ch + '\'s in the word.')
            print('You are completely hung：(')
            break
    print('The word was: ' + answer)


def dashed(answer):
    # Display the number of characters with dashes at the beginning.
    ans = ''
    print('The word looks like: ', end='')
    for i in range(len(answer)):
        ans += '-'
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
