#A simple Rock Paper Scissors game

from random import randint as rint

moves = ["rock", "paper", "scissors", "q"]
game = True
moveindex = {"r":0, "p":1, "s":2, "q":3}
win = 0
tie = 0
loss = 0

while game == True:
    print("Wins:", win,"\nTies:", tie,"\nLosses:", loss)
    cpumoven = rint(0,2)
    cpumove = moves[cpumoven]
    try:
        ipmove = moveindex[input("Choose your move by typing the first letter ex Rock = r. q to quit")]
        pmove = moves[ipmove]
        if pmove == "q":
            break
        if pmove == cpumove:
            tie += 1
            print("It is a tie!")

        elif pmove == "rock" and cpumove == "scissors":
            win += 1
        elif pmove == "paper" and cpumove == "rock":
            win += 1
        elif pmove == "scissors" and cpumove == "paper":
            win += 1
        else:
            loss += 1

        print("Your move:", pmove, "cpumove:", cpumove)
    except:
        print("Invalid Input")