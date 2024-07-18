"""
Connect4_Game:
class that creates a Connect4 game that runs
and takes inputs through a PyGame GUI
"""

import pygame
import sys
import math

# constants/pygame init
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COL_COUNT = 7
TILE_SIZE = 80
RADIUS = int(TILE_SIZE / 2 - 5)
BOARD = [[0] * COL_COUNT for _ in range(ROW_COUNT)]

pygame.init()

WIDTH = COL_COUNT * TILE_SIZE
HEIGHT = (ROW_COUNT + 1) * TILE_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("monospace", 50)


# draw blue square with black holes
# to represent the connect4 frame
def draw_board():
    pygame.draw.rect(
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
            pygame.draw.circle(
                SCREEN,
                BLACK,
                (
                    int(c * TILE_SIZE + TILE_SIZE / 2),
                    int(r * TILE_SIZE + TILE_SIZE + TILE_SIZE / 2),
                ),
                RADIUS,
            )
    pygame.display.update()


# drops a piece by player on col
def drop_piece(col, player):
    # find next empty space in col
    r = 0
    while BOARD[r][col] != 0:
        r += 1

    BOARD[r][col] = 1 if player == RED else 2

    # change appropriate circle color
    pygame.draw.circle(
        SCREEN,
        player,
        (
            int(col * TILE_SIZE + TILE_SIZE / 2),
            HEIGHT - int(r * TILE_SIZE + TILE_SIZE / 2),
        ),
        RADIUS,
    )
    pygame.display.update()

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
    pygame.draw.rect(SCREEN, BLACK, (0, 0, WIDTH, TILE_SIZE))

    # make sure no overflow
    posx = max(RADIUS, min(posx, WIDTH - RADIUS))

    # make sure circle is of correct color
    pygame.draw.circle(SCREEN, player, (posx, int(TILE_SIZE / 2)), RADIUS)
    pygame.display.update()


# main runloop
def run():
    draw_board()

    game_over = False
    player_turn = RED

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # moving circle that follows mouse
            if event.type == pygame.MOUSEMOTION:
                update_piece(player_turn, event.pos[0])

            if event.type == pygame.MOUSEBUTTONDOWN:
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
                            pygame.display.update()
                            game_over = True
                        # tie case
                        if board_filled():
                            label = FONT.render("TIE", 1, (255, 255, 255))
                            SCREEN.blit(label, (TILE_SIZE, 10))
                            pygame.display.update()
                            game_over = True

                    # player 2 input
                    else:
                        if drop_piece(selection, player_turn):
                            label = FONT.render("Player 2 Wins!", 1, YELLOW)
                            SCREEN.blit(label, (TILE_SIZE, 10))
                            pygame.display.update()
                            game_over = True
                        if board_filled():
                            label = FONT.render("TIE", 1, (255, 255, 255))
                            SCREEN.blit(label, (TILE_SIZE, 10))
                            pygame.display.update()
                            game_over = True

                    # alternate between players
                    player_turn = YELLOW if player_turn == RED else RED

                    if not game_over:
                        update_piece(player_turn, posx)

    pygame.time.wait(2000)


if __name__ == "__main__":
    run()
