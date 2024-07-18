"""
Connect4_Game:
class that creates a Connect4 game that runs
and takes inputs through the terminal
"""


class Connect4_Game:

    # creates board using a 2d array of 0s
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0] * cols for _ in range(rows)]

    # helper function to check if board is filled (tie)
    def __board_filled(self):
        for i in range(self.rows):
            if self.board[i][5] == 0:
                return False
        return True

    # helper function to check if a move is valid
    def __valid_move(self, col):
        # check that input is an int
        try:
            col = int(col)
        except:
            return False

        # checks that top row of the column is not filled
        # and within the boundaries of the grid
        if self.board[5][col] != 0 and 0 <= col <= self.cols:
            print("Invalid Move")
            return False
        return True

    # drops a piece by player on col
    def __drop_piece(self, col, player):
        # find next empty space in col
        r = 0
        while self.board[r][col] != 0:
            r += 1
        self.board[r][col] = player

        # check if new piece creates a win
        return self.__win_condition(r, col, player)

    # formats and prints the board
    def __print_board(self):
        for r in reversed(range(len(self.board))):
            s = "| "
            for c in range(len(self.board[0])):
                i = self.board[r][c]
                s += str(i)
                s += " | "
            print(s)

    # helper function to count pieces in a certain direction'
    # (dr dc inputs being the changes in x and y)
    def __count_direction(self, row, col, dr, dc, player):
        count = 0
        r, c = row + dr, col + dc
        # iterate over that direction until an edge or non player tile is reached
        while (
            0 <= r < len(self.board)
            and 0 <= c < len(self.board[0])
            and self.board[r][c] == player
        ):
            count += 1
            r += dr
            c += dc
        return count

    # function to check for a win after a new piece is placed
    def __win_condition(self, row, col, player):
        # check all directions
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            count += self.__count_direction(row, col, dr, dc, player)
            count += self.__count_direction(row, col, -dr, -dc, player)
            if count >= 4:
                return True
        return False

    # main runloop
    def run(self):
        game_over = False
        player_turn = 0

        while not game_over:
            self.__print_board()

            # player 1 input
            if player_turn == 0:
                # takes column input
                selection = input("Player 1 Move (0-6): ")

                # check for valid move and take input until valid
                while not self.__valid_move(selection):
                    print("invalid")
                    selection = input("Player 1 Move (0-6): ")

                selection = int(selection)
                # drop piece and check for win
                if self.__drop_piece(selection, 1):
                    game_over = True
                    print("Player 1 Wins")
                # tie case
                if self.__board_filled():
                    game_over = True
                    print("Tie")

            # player 2 input
            else:
                selection = input("Player 2 Move (0-6): ")

                while not self.__valid_move(selection):
                    selection = input("Player 2 Move (0-6): ")

                selection = int(selection)
                if self.__drop_piece(selection, 2):
                    game_over = True
                    print("Player 2 Wins")
                if self.__board_filled():
                    game_over = True
                    print("Tie")

            # alternate between players
            player_turn = (player_turn + 1) % 2


if __name__ == "__main__":
    game = Connect4_Game(6, 7)
    game.run()
