# pip install pygame
# pip install dokusan

import pygame
import sys
import numpy as np
from SudokuSolver import Sudoku_Solver
# temporary
from dokusan import generators

sys.dont_write_bytecode = True
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
GREY = (105, 105, 105)
LIGHT_GREY = (211, 211, 211)
FPS = 60
SCREEN_WIDTH = 550
BUFF = 6

pygame.init()
pygame.display.set_caption("Sudoku")
CLOCK = pygame.time.Clock()
standard_font = pygame.font.SysFont("Comic Sans MS", 35)
screen = pygame.display.set_mode((SCREEN_WIDTH, 650))


def main():
    board_original, board = create_game_board()
    auto_solver(board_original)  # temporary
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                # splits screen into grid of 50x50 squares
                pos = (pos[0]//50, pos[1]//50)
                i, j = pos[0], pos[1]
                # print(i, j)
                # checks if mouse input is within the sudoku grid
                if (1 <= i <= 9 and 1 <= j <= 9):
                    # print(board_original[j-1][i-1])
                    # check if the selected square is a fixed value
                    if (str(board_original[j-1][i-1]) == str(0)):
                        val = board[j-1][i-1]
                        # print(val)
                        pygame.draw.rect(screen, LIGHT_GREY,
                                         (i*50+BUFF, j*50+BUFF, 40, 40))
                        if (val != 0):    # re-prints the value only if its non-zero
                            value = standard_font.render(val, True, GREY)
                            screen.blit(value, (i*50+15, j*50))
                        pygame.display.update()
                        insert(screen, board, board_original, pos)
                        # print(board)
                    else:
                        pass
        pygame.display.update()
        CLOCK.tick(FPS)


def create_game_board():   # creates game board with puzzle grid
    grid_original = np.array(
        list(str(generators.random_sudoku(avg_rank=150)))).reshape(9, 9)
    grid = [[0 for i in range(9)] for j in range(9)]
    for r in range(9):
        for c in range(9):
            grid[r][c] = int(grid_original[r][c])
    screen.fill(WHITE)
    for i in range(10):    # creates grid lines
        width = 4 if (i % 3 == 0) else 2
        pygame.draw.line(screen, BLACK, (50*(i+1), 50),
                         (50*(i+1), 500), width)
        pygame.draw.line(screen, BLACK, (50, 50*(i+1)),
                         (500, 50*(i+1)), width)
    for i in range(9):    # applies fixed values to the game board
        for j in range(9):
            if (grid[i][j] != 0):   # only prints non-zero numbers
                value = standard_font.render(
                    str(grid[i][j]), True, BLACK)
                screen.blit(value, ((j+1)*50+15, (i+1)*50))
    return grid_original, grid


def insert(screen, grid, grid_original, pos):
    i, j = pos[0], pos[1]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (grid_original[j-1][i-1] != str(0)):    # checks original grid
                    return
                elif (event.key == 8):    # clears the grid if backspace is pressed
                    grid[j-1][i-1] = str(0)
                    pygame.draw.rect(
                        screen, WHITE, (i*50+BUFF, j*50+BUFF, 40, 40))
                    pygame.display.update()
                    return
                elif (48 < event.key < 58):    # if between 1-9 prints to grid
                    grid[j-1][i-1] = str(event.key-48)
                    pygame.draw.rect(
                        screen, WHITE, (i*50+BUFF, j*50+BUFF, 40, 40))
                    value = standard_font.render(
                        str(event.key-48), True, GREY)
                    screen.blit(value, (i*50+15, j*50))
                    pygame.display.update()
                    return
                return


def auto_solver(grid_original):
    solver = Sudoku_Solver(grid_original)
    solution, count = solver.solve()
    print(np.array(solution))
    print("count: "+str(count))


if __name__ == "__main__":
    main()
