##Create a program that will play the “cows and bulls” game with the user. The game works like this: Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.##

from pickle import TRUE
import random
from collections import Counter

def generateNumber():
    secret = []
    while len(secret) < 4:
        num = random.randint(1,9)
        if num not in secret:
            secret.append(num)
    return secret


def playGame():
    bulls, cows = 0,0
    attemps = 0

    choice = input("Please enter a 4 digit number: ")
    guess = list(choice)
    guess = [eval(i) for i in guess]
    #secret = generateNumber()
    secret = 1234
    playing = True
    
    while playing:
        for x,y in zip(guess,secret):
            if y in guess:
                if y == x:
                    cows+= 1
                else:
                    bulls += 1

    

playGame()






