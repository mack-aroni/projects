import random as rand
import numpy as np

class minesweeper:

    """
    init(num, size):
    creates the static board of size x size with num amount of mines
    """
    def __init__(self, num, size):
        self.count = 0
        self.size = size
        self.num = num
        self.mainBoard = np.array(
            [["-" for i in range(size)] for i in range(size)])
        self.gameBoard = np.array(
            [["?" for i in range(size)] for i in range(size)])
        c = 0
        while c < num:
            x = int(rand.random()*size)
            y = int(rand.random()*size)
            if self.mainBoard[x][y] == "-":
                self.mainBoard[x][y] = "*"
                c = c + 1

    """
    isValid(r,c):
    checks if the coordinates are on the grid
    and if so returns if the grid contains a mine
    """
    def isValid(self, x, y):
        return x >= 0 and x < self.size and y >= 0 and y < self.size

    """
    hasMine(x, y):
    returns if the tile contains a mine
    """
    def hasMine(self, x, y):
        if self.isValid(x,y):
            return self.mainBoard[x][y] == "*"

    """
    chooseTile(x,y):
    picks the tile at the x and y coordinate
    if the tile is a bomb returns false
    if 
    """
    def chooseTile(self, x, y):
        if self.mainBoard[x][y] == "*":
            #temp
            print("Gameover")
            return
        c = 0
        # left cell
        if self.hasMine(x-1, y):
            c = c + 1
        # top left cell
        if self.hasMine(x-1, y-1):
            c = c + 1
        # bottom left cell
        if self.hasMine(x-1, y+1):
            c = c + 1
        # top cell
        if self.hasMine(x, y-1):
            c = c + 1
        # bottom cell
        if self.hasMine(x, y+1):
            c = c + 1
        # right cell
        if self.hasMine(x+1, y):
            c = c + 1
        # top right cell
        if self.hasMine(x+1, y-1):
            c = c + 1
        # bottom right cell
        if self.hasMine(x+1, y+1):
            c = c + 1
        # temp
        print("Tile: "+str(x+1)+","+str(y+1)+" count: "+str(c))
        # changes the value of the tile to count
        self.gameBoard[x][y] = str(c)
        self.count = self.count + 1
        # if count == 0 recursively iterate until all connecting tiles have count > 0
        if c == 0:
            # left cell
            if self.isValid(x-1, y):
                if self.gameBoard[x-1][y] == "?":
                    self.chooseTile(x-1,y)
            # top left cell
            if self.isValid(x-1, y-1):
                if self.gameBoard[x-1][y-1] == "?":
                    self.chooseTile(x-1,y-1)
            # bottom left cell
            if self.isValid(x-1, y+1):
                if self.gameBoard[x-1][y+1] == "?":
                    self.chooseTile(x-1,y+1)    
            # top cell
            if self.isValid(x, y-1):
                if self.gameBoard[x][y-1] == "?":
                    self.chooseTile(x,y-1)
            # bottom cell
            if self.isValid(x, y+1):
                if self.gameBoard[x][y+1] == "?":
                    self.chooseTile(x,y+1)
            # right cell
            if self.isValid(x+1, y):
                if self.gameBoard[x+1][y] == "?":
                    self.chooseTile(x+1,y)
            # top right cell
            if self.isValid(x+1, y-1):
                if self.gameBoard[x+1][y-1] == "?":
                    self.chooseTile(x+1,y-1)
            # bottom right cell
            if self.isValid(x+1, y+1):
                if self.gameBoard[x+1][y+1] == "?":
                    self.chooseTile(x+1,y+1)
        
    """
    run():
    main run loop for minesweeper game
    """
    def run(self):
        game.printBoard(game.mainBoard)
        s = input("(row,col): ")
        while self.count == (self.size * self.size - self.num) or s != "end":
            s = s.split(" ")
            game.chooseTile(int(s[0])-1,int(s[1])-1)
            game.printBoard(game.gameBoard)
            s = input("(row,col): ")

    """
    printBoard():
    formats and prints board
    """
    def printBoard(self,board):
        # prints top column counter
        s = "    "
        for i in range(size):
            if i < 9:
                s = s + "  " + str(i+1) + " "
            else:
                s = s + "  " + str(i+1)
        print(s)
        # prints side row counter with row contents
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
    size = 2#9
    num = 1#10
    game = minesweeper(num,size)
    game.run()