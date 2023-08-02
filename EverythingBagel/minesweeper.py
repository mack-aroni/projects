import random as rand

class minesweeper:

    """
    init(num,size):
    creates the static board of size x size with num amount of mines
    """
    def __init__(self, num, size):
        self.count = 0
        self.size = size
        self.num = num
        self.mainBoard = [["-" for i in range(size)] for i in range(size)]
        self.gameBoard = [["?" for i in range(size)] for i in range(size)]
        c = 0
        while c < num:
            x = int(rand.random()*size)
            y = int(rand.random()*size)
            if self.mainBoard[x][y] == "-":
                self.mainBoard[x][y] = "*"
                c = c + 1

    """
    isValid(r,c):
    private method that checks if the coordinates
    are within the bounds of the grid
    """
    def __isValid(self, x, y):
        return x >= 0 and x < self.size and y >= 0 and y < self.size

    """
    countAdjacent(x,y,sym):
    private method that returns if the tile
    contains the input symbol
    """
    def __countAdjacent(self, x, y, sym):
        c = 0
        # left cell
        if self.__isValid(x-1, y) and self.mainBoard[x-1][y] == sym:
            c = c + 1
        # top left cell
        if self.__isValid(x-1, y-1) and self.mainBoard[x-1][y-1] == sym:
            c = c + 1
        # bottom left cell
        if self.__isValid(x-1, y+1) and self.mainBoard[x-1][y+1] == sym:
            c = c + 1
        # top cell
        if self.__isValid(x, y-1) and self.mainBoard[x][y-1] == sym:
            c = c + 1
        # bottom cell
        if self.__isValid(x, y+1) and self.mainBoard[x][y+1] == sym:
            c = c + 1
        # right cell
        if self.__isValid(x+1, y) and self.mainBoard[x+1][y] == sym:
            c = c + 1
        # top right cell
        if self.__isValid(x+1, y-1) and self.mainBoard[x+1][y-1] == sym:
            c = c + 1
        # bottom right cell
        if self.__isValid(x+1, y+1) and self.mainBoard[x+1][y+1] == sym:
            c = c + 1
        return c
    
    """
    chooseTile(x,y):
    picks the tile at the x and y coordinate
    if the tile is a mine returns 0 else returns
    1 if all non-mine tiles have been revealed
    """
    def chooseTile(self, x, y):
        # mine was selected
        if self.mainBoard[x][y] == "*":
            return 0
        # already revealed tile was selected
        if self.gameBoard[x][y] != "?":
            return
        # changes the value of the tile to count
        c = self.__countAdjacent(x,y,"*")
        self.gameBoard[x][y] = str(c)
        self.count = self.count + 1
        
        # temp
        #print("Tile: "+str(x+1)+","+str(y+1)+" count: "+str(c)+" c: "+str(self.count))
        
        # if count == 0 recursively iterate until all 
        # connecting tiles have count > 0
        if c == 0:
            # left cell
            if self.__isValid(x-1, y) and self.gameBoard[x-1][y] == "?":
                self.chooseTile(x-1,y)
            # top left cell
            if self.__isValid(x-1, y-1) and self.gameBoard[x-1][y-1] == "?":
                self.chooseTile(x-1,y-1)
            # bottom left cell
            if self.__isValid(x-1, y+1) and self.gameBoard[x-1][y+1] == "?":
                self.chooseTile(x-1,y+1)    
            # top cell
            if self.__isValid(x, y-1) and self.gameBoard[x][y-1] == "?":
                self.chooseTile(x,y-1)
            # bottom cell
            if self.__isValid(x, y+1) and self.gameBoard[x][y+1] == "?":
                self.chooseTile(x,y+1)
            # right cell
            if self.__isValid(x+1, y) and self.gameBoard[x+1][y] == "?":
                self.chooseTile(x+1,y)
            # top right cell
            if self.__isValid(x+1, y-1) and self.gameBoard[x+1][y-1] == "?":
                self.chooseTile(x+1,y-1)
            # bottom right cell
            if self.__isValid(x+1, y+1) and self.gameBoard[x+1][y+1] == "?":
                self.chooseTile(x+1,y+1)
        # all non-mine tiles have been selected
        if self.count == (self.size * self.size - self.num):
            return 1
        # confirmation of a regular action
        return 2
        
    """
    flagTile(x,y):
    flags the tile as long as it hasn't been
    revealed, can also unflag the same way
    """
    def flagTile(self, x, y):
        if self.gameBoard[x][y] == "?":
            self.gameBoard[x][y] = "!"
        elif self.gameBoard[x][y] == "!":
            self.gameBoard[x][y] = "?"
        # confirmation of regular action
        return 2
      
    """
    run():
    main run loop for minesweeper game
    """
    def run(self):
        # temp prints mainBoard with mines
        game.printBoard(game.mainBoard)
        game.printBoard(game.gameBoard)
        while True:
            # breaks down input
            s = input("(row,col): ").split(" ")
            # variable holds action results
            r = None

            # input break case
            if len(s) == 1 and s[0] == "end":
                break

            # flagging case
            if len(s) == 3:
                try:
                    if s[0] == "flag" and self.__isValid(int(s[1])-1, int(s[2])-1):
                        r = game.flagTile(int(s[1])-1,int(s[2])-1)
                except:
                    None

            # tile choosing case
            if len(s) == 2:
                try:
                    if self.__isValid(int(s[0])-1, int(s[1])-1):
                        r = game.chooseTile(int(s[0])-1,int(s[1])-1)
                except:
                    None

            # indicates mine was selected
            if r == 0:
                print("Game Over")
                break
            # indicates all non-mine tiles were revealed
            elif r == 1:
                print("You Win")
                break
            # input loop was satisfied and a regular action
            # was performed, displaying the changed board
            elif r == 2:
                game.printBoard(game.gameBoard)


    """
    printBoard():
    formats and prints board
    """
    def printBoard(self,board):
        # prints top column counter
        s = "    "
        for i in range(self.size):
            if i < 9:
                s = s + "  " + str(i+1) + " "
            else:
                s = s + "  " + str(i+1)
        print(s)
        # prints side row counter with row contents
        for r in range(self.size):
            if r < 9:
                s = str(r+1) + "   "
            else:
                s = str(r+1) + "  "
            for c in range(self.size):
                s = s + "| " + str(board[r][c]) + " "
            s = s + "| "
            print(s)

if __name__ == "__main__":
    BEGINNER = [10,9]
    game = minesweeper(BEGINNER[0],BEGINNER[1])
    game.run()