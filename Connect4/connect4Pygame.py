import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


# helper function to check if a move is valid
def valid_move(col):
    # checks that top row of the column is not filled
    # and within the boundaries of the grid
    if BOARD[5][col] != 0 and 0 <= col <= COL_COUNT:
        return False
    return True


# drops a piece by player on col
def drop_piece(col, player):
    # find next empty space in col
    r = 0
    while BOARD[r][col] != 0:
        r += 1

    BOARD[r][col] = player

    # change appropriate circle color
    if player_turn == 0:
        pygame.draw.circle(
            SCREEN,
            RED,
            (
                int(col * TILE_SIZE + TILE_SIZE / 2),
                height - int(r * TILE_SIZE + TILE_SIZE / 2),
            ),
            RADIUS,
        )
    else:
        pygame.draw.circle(
            SCREEN,
            YELLOW,
            (
                int(col * TILE_SIZE + TILE_SIZE / 2),
                height - int(r * TILE_SIZE + TILE_SIZE / 2),
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
    r, c = row + dr, col + dc
    # iterate over that direction until an edge or non player tile is reached
    while 0 <= r < len(BOARD) and 0 <= c < len(BOARD[0]) and BOARD[r][c] == player:
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


#  updates the moving piece color
def update_piece(player):
    pygame.draw.rect(SCREEN, BLACK, (0, 0, width, TILE_SIZE))
    posx = event.pos[0]

    # make sure no overflow
    if posx < RADIUS:
        posx = RADIUS
    elif posx > width - RADIUS:
        posx = width - RADIUS

    # make sure circle is of correct color
    if player == 0:
        pygame.draw.circle(SCREEN, RED, (posx, int(TILE_SIZE / 2)), RADIUS)
    else:
        pygame.draw.circle(SCREEN, YELLOW, (posx, int(TILE_SIZE / 2)), RADIUS)
    pygame.display.update()


# execution start
pygame.init()

ROW_COUNT = 6
COL_COUNT = 7
TILE_SIZE = 80
BOARD = [[0] * COL_COUNT for _ in range(ROW_COUNT)]

width = COL_COUNT * TILE_SIZE
height = (ROW_COUNT + 1) * TILE_SIZE
size = (width, height)
SCREEN = pygame.display.set_mode(size)
RADIUS = int(TILE_SIZE / 2 - 5)
FONT = pygame.font.SysFont("monospace", 50)

# draw blue square with black holes
# to represent the connect 4 frame
pygame.draw.rect(
    SCREEN,
    BLUE,
    (
        0,
        TILE_SIZE,
        width,
        height,
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

game_over = False
player_turn = 0

# main runloop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # moving circle that follows mouse
        if event.type == pygame.MOUSEMOTION:
            update_piece(player_turn)

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            selection = math.floor(posx / TILE_SIZE)

            # check valid move
            if valid_move(selection):

                # player 1 input
                if player_turn == 0:
                    # check winning move
                    if drop_piece(selection, 1):
                        label = FONT.render("Player 1 Wins!", 1, RED)
                        SCREEN.blit(label, (TILE_SIZE, 10))
                        pygame.display.update()
                        game_over = True

                # player 2 input
                else:
                    if drop_piece(selection, 2):
                        label = FONT.render("Player 2 Wins!", 1, YELLOW)
                        SCREEN.blit(label, (TILE_SIZE, 10))
                        pygame.display.update()
                        game_over = True

                # alternate between players
                player_turn = (player_turn + 1) % 2
                update_piece(player_turn)

pygame.time.wait(2000)
