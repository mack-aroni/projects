"""
Connect4_Game:
class that creates a Connect4 game that runs
and takes inputs through a PyGame GUI and contains a
minimax algorithm AI player
"""

import pygame
import sys
import math
import random


import numpy as np

# constants/pygame init
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COL_COUNT = 7
TILE_SIZE = 80
RADIUS = int(TILE_SIZE / 2 - 5)

pygame.init()
WIDTH = COL_COUNT * TILE_SIZE
HEIGHT = (ROW_COUNT + 1) * TILE_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("monospace", 50)


# draw blue square with black holes
# to represent the connect4 frame
def draw_screen():
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
def drop_piece(board, col, player):
    # find next empty space in col
    r = 0
    while board[r][col] != 0:
        r += 1

    board[r][col] = 1 if player == RED else 2

    # check if new piece creates a win
    return win_condition(board, r, col, player)


# helper function to count pieces in a certain direction
# (dr dc inputs being the changes in x and y)
def count_direction(board, row, col, dr, dc, player):
    count = 0
    num = 1 if player == RED else 2
    r, c = row + dr, col + dc
    # iterate over that direction until an edge or non player tile is reached
    while 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == num:
        count += 1
        r += dr
        c += dc
    return count


# function to check for a win after a new piece is placed
def win_condition(board, row, col, player):
    # check all directions
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        count += count_direction(board, row, col, dr, dc, player)
        count += count_direction(board, row, col, -dr, -dc, player)
        if count >= 4:
            return True
    return False


#  updates the moving piece color
def update_piece(player, posx):
    pygame.draw.rect(SCREEN, BLACK, (0, 0, WIDTH, TILE_SIZE))

    # make sure no overflow
    posx = max(RADIUS, min(posx, WIDTH - RADIUS))

    # make sure circle is of correct color
    pygame.draw.circle(SCREEN, player, (posx, int(TILE_SIZE / 2)), RADIUS)
    pygame.display.update()


# updates the board by filling in pieces dropped
def update_screen(board):
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            if board[r][c] != 0:
                color = RED if board[r][c] == 1 else YELLOW
                pygame.draw.circle(
                    SCREEN,
                    color,
                    (
                        int(c * TILE_SIZE + TILE_SIZE / 2),
                        HEIGHT - int(r * TILE_SIZE + TILE_SIZE / 2),
                    ),
                    RADIUS,
                )
    pygame.display.update()


# helper function that finds all available moves
# and returns them in the form of a list of tuples
def available_moves(board):
    moves = []
    for c in range(COL_COUNT):
        r = 0
        while r < ROW_COUNT and board[r][c] != 0:
            r += 1
        if r < ROW_COUNT:
            moves.append((r, c))
    return moves


# helper function that evaluates all possible
# moves by a player on a given board
# and returns them with a heuristic value
def eval_moves(board, moves, player):
    rank_moves = []
    for m in moves:
        tempboard = [row[:] for row in board]
        drop_piece(tempboard, m[1], player)
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        temp = []

        for dr, dc in directions:
            count = 1
            count += count_direction(tempboard, m[0], m[1], dr, dc, player)
            count += count_direction(tempboard, m[0], m[1], -dr, -dc, player)
            temp.append(count)

        if temp:
            rank_moves.append((m, max(temp)))

    # print(rank_moves)
    return rank_moves


# helper function that sorts all possible moves
# on a board and returns the column of the best option
def best_move(board, moves):
    max = 0
    for i in range(len(moves)):
        if moves[i][1] == 100:
            return moves[i][0]
        if moves[i][1] > max:
            max = i

    return moves[max][0]


# main call function for AI minimax algorithm
def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = available_moves(board)
    print(valid_locations)

    # end of depth returns best possible move
    if depth == 0:
        sort = eval_moves(board, valid_locations, YELLOW)
        print("sort", sort)
        return (None, sort[0][1])

    # no more valid moves
    if len(valid_locations) == 0:
        return (None, 0)

    # maximizing player score
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for m in valid_locations:
            b_copy = [row[:] for row in board]
            if drop_piece(b_copy, m[1], YELLOW):
                return (None, 1000)
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = m[1]
            if max(alpha, value) >= beta:
                break
        return column, value
    # minimizing opponent score
    else:
        value = math.inf
        column = random.choice(valid_locations)
        for m in valid_locations:
            b_copy = [row[:] for row in board]
            if drop_piece(b_copy, m[1], RED):
                return (None, -1000)
            new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = m[1]
            if alpha >= max(beta, value):
                break
        return column, value


# main runloop
def run():
    board = [[0] * COL_COUNT for _ in range(ROW_COUNT)]
    draw_screen()

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
                if board[5][selection] == 0:

                    # player 1 input
                    if player_turn == RED:
                        # check for winning move
                        game_over = drop_piece(board, selection, player_turn)
                        update_screen(board)
                        if game_over:
                            label = FONT.render("Player 1 Wins!", 1, RED)
                            SCREEN.blit(label, (TILE_SIZE, 10))
                            pygame.display.update()

                    # change turns
                    player_turn = YELLOW

        # AI turn
        if player_turn == YELLOW and not game_over:
            # moves = available_moves(board)
            # moves = eval_moves(board, moves, player_turn)
            # move = best_move(board, moves)
            col, score = minimax(board, 3, -math.inf, math.inf, True)
            print("col", col, "score", score)

            game_over = drop_piece(board, col, player_turn)
            update_screen(board)
            if game_over:
                label = FONT.render("Player 2 Wins!", 1, YELLOW)
                SCREEN.blit(label, (TILE_SIZE, 10))
                pygame.display.update()

            # change turns
            player_turn = RED

    pygame.time.wait(2000)


if __name__ == "__main__":
    run()
