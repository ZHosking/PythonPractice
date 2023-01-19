##Make a two-player Rock-Paper-Scissors game.##

userA = input("Enter your name: ")
userB = input("Enter your name: ")

inputA = input("%s, input your move: " % userA)
inputB = input("%s, input your move: " % userB)

def game(iA, iB):
    if iA == iB:
        print("Game is a draw!")
    elif iA == "rock":
        if iB == "scissors":
            return(userA + " wins!")
        else:
            return(userB + " wins!"
            )
    elif iA == "paper":
        if iB == "rock":
            return(userA + " wins!")
        else:
            return(userB + " wins!")
    elif iA == "scissors":
        if iB == "paper":
            return(userA + " wins!")
        else:
            return(userB + " wins!")
    else: 
        return("Invalid input - Please enter rock, paper or scissors!")
        sys.exit()

print(game(inputA, inputB))
