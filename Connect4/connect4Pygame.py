"""
Connect4_Game:
class that creates a Connect4 game that runs
and takes inputs through a py GUI
"""

import pygame as py
import sys
import math

# constants/py init
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COL_COUNT = 7
TILE_SIZE = 80
RADIUS = int(TILE_SIZE / 2 - 5)
BOARD = [[0] * COL_COUNT for _ in range(ROW_COUNT)]

py.init()

WIDTH = COL_COUNT * TILE_SIZE
HEIGHT = (ROW_COUNT + 1) * TILE_SIZE
SCREEN = py.display.set_mode((WIDTH, HEIGHT))
FONT = py.font.SysFont("monospace", 50)


# draw blue square with black holes
# to represent the connect4 frame
def draw_board():
    py.draw.rect(
        SCREEN,
        BLUE,
        (
            0,
            TILE_SIZE,
            WIDTH,
            HEIGHT,
        ),
    )
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            py.draw.circle(
                SCREEN,
                BLACK,
                (
                    int(c * TILE_SIZE + TILE_SIZE / 2),
                    int(r * TILE_SIZE + TILE_SIZE + TILE_SIZE / 2),
                ),
                RADIUS,
            )
    py.display.update()


# drops a piece by player on col
def drop_piece(col, player):
    # find next empty space in col
    r = 0
    while BOARD[r][col] != 0:
        r += 1

    BOARD[r][col] = 1 if player == RED else 2

    # change appropriate circle color
    py.draw.circle(
        SCREEN,
        player,
        (
            int(col * TILE_SIZE + TILE_SIZE / 2),
            HEIGHT - int(r * TILE_SIZE + TILE_SIZE / 2),
        ),
        RADIUS,
    )
    py.display.update()

    # check if new piece creates a win
    return win_condition(r, col, player)


# helper function to count pieces in a certain direction
# (dr dc inputs being the changes in x and y)
def count_direction(row, col, dr, dc, player):
    count = 0
    num = 1 if player == RED else 2
    r, c = row + dr, col + dc
    # iterate over that direction until an edge or non player tile is reached
    while 0 <= r < len(BOARD) and 0 <= c < len(BOARD[0]) and BOARD[r][c] == num:
        count += 1
        r += dr
        c += dc
    return count


# function to check for a win after a new piece is placed
def win_condition(row, col, player):
    # check all directions
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        count += count_direction(row, col, dr, dc, player)
        count += count_direction(row, col, -dr, -dc, player)
        if count >= 4:
            return True
    return False


# helper function to check if board is filled (tie)
def board_filled():
    for i in range(ROW_COUNT):
        if BOARD[i][5] == 0:
            return False
    return True


#  updates the moving piece color
def update_piece(player, posx):
    py.draw.rect(SCREEN, BLACK, (0, 0, WIDTH, TILE_SIZE))

    # make sure no overflow
    posx = max(RADIUS, min(posx, WIDTH - RADIUS))

    # make sure circle is of correct color
    py.draw.circle(SCREEN, player, (posx, int(TILE_SIZE / 2)), RADIUS)
    py.display.update()


# main runloop
def run():
    draw_board()

    game_over = False
    player_turn = RED

    while not game_over:

        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()

            # moving circle that follows mouse
            if event.type == py.MOUSEMOTION:
                update_piece(player_turn, event.pos[0])

            if event.type == py.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                selection = math.floor(posx / TILE_SIZE)

                # checks that top row of the column is not filled
                if BOARD[5][selection] == 0:

                    # player 1 input
                    if player_turn == RED:
                        # check winning move
                        if drop_piece(selection, player_turn):
                            label = FONT.render("Player 1 Wins!", 1, RED)
                            SCREEN.blit(label, (TILE_SIZE, 10))
                            py.display.update()
                            game_over = True
                        # tie case
                        if board_filled():
                            label = FONT.render("TIE", 1, (255, 255, 255))
                            SCREEN.blit(label, (TILE_SIZE, 10))
                            py.display.update()
                            game_over = True

                    # player 2 input
                    else:
                        if drop_piece(selection, player_turn):
                            label = FONT.render("Player 2 Wins!", 1, YELLOW)
                            SCREEN.blit(label, (TILE_SIZE, 10))
                            py.display.update()
                            game_over = True
                        if board_filled():
                            label = FONT.render("TIE", 1, (255, 255, 255))
                            SCREEN.blit(label, (TILE_SIZE, 10))
                            py.display.update()
                            game_over = True

                    # alternate between players
                    player_turn = YELLOW if player_turn == RED else RED

                    if not game_over:
                        update_piece(player_turn, posx)

    py.time.wait(2000)


if __name__ == "__main__":
    run()
