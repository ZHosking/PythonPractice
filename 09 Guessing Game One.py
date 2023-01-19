##Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.##

import random

def get_ranNumber():
    return random.randint(1, 9)

def main():
    number = get_ranNumber()
    numGuesses = 0
    userGuess = 0
    
    while userGuess != "exit":
        userGuess = input("Enter guess between 1 & 9: ")

        if userGuess == "exit":
            break

        userGuess = int(userGuess)
        numGuesses += 1

        if userGuess < number:
            print("Guess is too low!")
        elif userGuess > number:
            print("Guess is too high!") 
        else:
            print("Guess is correct!")
            print("It took you", str(numGuesses), " tries!")

main()







