import random


def sum(a, b, c):
    return a + b + c


def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")     #string formatting
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")


def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print(player1," Won the match")
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print(player2," Won the match")
            return 0

    return -1



xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print("Welcome to Tic Tac Toe")
print("Instructions:\n 1. Toss(Player 1-Tails & Player 2-Heads.) \n 2. Insert the spot number(0-8) to put your sign. \n 3. Fill all spots to get result")
player1=input("Enter the Player 1 name : ")
player2=input("Enter The Player 2 name : ")

print("Lets coin the toss :")
toss = random.randint(0, 1)     #for toss random funcn
#print(toss)
if toss == 0:
    print("Its Heads ," ,player2, " won the toss !")
else:
    print("Its Tails ," , player1," won the toss !")
   # 1 for Tails and 0 for Heads


while (True):      # to make loop run forever
    printBoard(xState, zState)      #function call for board printing
    if (toss == 1):
        print(player1, "'s Chance")
        value = int(input("Please enter a value: "))
        xState[value] = 1
    else:
        print(player2, "'s Chance")
        value = int(input("Please enter a value: "))
        zState[value] = 1
    cwin = checkWin(xState, zState)
    if (cwin != -1):
        print("Match over")
        break

    toss = 1 - toss