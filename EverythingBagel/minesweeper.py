import random as rand
import numpy as np

"""
createBoard(num, size):
function that creates the static board of
size x size with num amount of mines
"""
def createBoard(num, size):
    mainBoard = np.array(
        [[0 for i in range(size)] for i in range(size)])
    c = 0
    while c < num:
        x = int(rand.random()*size)
        y = int(rand.random()*size)
        if mainBoard[x][y] == 0:
            mainBoard[x][y] = 1
            c = c + 1
    return mainBoard

"""
printBoard(board):
formats and prints the input board
"""
def printBoard(board):
    s = "    "
    for i in range(size):
        if i < 9:
            s = s + "  " + str(i+1) + " "
        else:
            s = s + "  " + str(i+1)
    print(s)
    for r in range(size):
        if r < 9:
            s = str(r+1) + "   "
        else:
            s = str(r+1) + "  "
        for c in range(size):
            s = s + "| " + str(board[r][c]) + " "
        s = s + "| "
        print(s)

if __name__ == "__main__":
    num = 10
    size = 9
    board = createBoard(num,size)
    printBoard(board)