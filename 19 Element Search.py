##Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.##

list = [3,5,6,8,12,16,18,20]

def getGuess():
    guess = int(input("Please enter a guess: "))
    if guess in list:
        print("Congratulations! Your number is in the list")
    else:
        print("Sorry your number is not in the list :(")

    print("")
    continueGame = input("Enter "'Yes'" to play again: ")
    if continueGame == 'Yes':
        getGuess()
    else:
        print("Thanks for playing!")

getGuess()