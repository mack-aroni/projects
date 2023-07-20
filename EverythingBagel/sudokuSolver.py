import numpy as np
from dokusan import generators

"""
Sudoku_Solver:
class that starts with a raw sudoku puzzle and outputs the completed puzzle
a class is used to better work with variables that would otherwise be glvoals
"""
class Sudoku_Solver:

    def __init__(self, origianal_grid):
        self.original_grid = original_grid
        # temp counter
        self.count = 0
        # new 9 by 9 grid 
        self.grid = [[0 for i in range(9)] for j in range(9)]
        # 3 by 3 grid that holds values True/Falso from 0-10
        self.subgrid_has_val = [
            [[False for i in range(10)] for j in range(3)] for k in range(3)]
        # all 9 rows that hold values 0-10
        self.row_has_val = [[False for i in range(10)] for j in range(9)]
        # all 9 columns that hold values 0-10
        self.col_has_val = [[False for i in range(10)] for j in range(9)]

    """
    placeVal(val, row, col):
    places the val at the specified value and updates the puzzle accordingly
    """
    def placeVal(self, val, row, col):
        self.grid[row][col] = val
        self.subgrid_has_val[row // 3][col // 3][val] = True
        self.row_has_val[row][val] = True
        self.col_has_val[col][val] = True

    """
    removeVal(val, row, col):
    removes the val at the specified value and updates the puzzle accordingly
    """
    def removeVal(self, val, row, col):
        self.grid[row][col] = 0
        self.subgrid_has_val[row // 3][col // 3][val] = False
        self.row_has_val[row][val] = False
        self.col_has_val[col][val] = False

    def isSafe(self, val, row, col):
        return not (self.row_has_val[row][val] or
                    self.col_has_val[col][val] or
                    self.subgrid_has_val[row // 3][col // 3][val])

    """
    solve(n):
    main recursive-backtracking solving function
    """
    def solveRB(self, n):
        self.count += 1
        row = n // 9
        col = n % 9
        if (n == 81):
            return True
        if (str(self.original_grid[row][col]) != "0"):
            return self.solveRB(n + 1)
        for i in range(1, 10):
            # print("i: "+str(i)+" row: "+str(row)+" " +str(row//3)+" col: "+str(col)+" "+str(col//3))
            if (self.isSafe(i, row, col)):
                self.placeVal(i, row, col)
                if (self.solveRB(n + 1)):
                    return True
                self.removeVal(i, row, col)
        return False

    """
    solve():
    calls solveRB and returns the finished puzzle
    """
    def solve(self):
        for r in range(9):
            for c in range(9):
                self.placeVal(int(self.original_grid[r][c]), r, c)
        foundSol = self.solveRB(0)
        if (foundSol):
            return self.grid, self.count

if __name__ == "__main__":
    original_grid = np.array(list(str(generators.random_sudoku(avg_rank=150)))).reshape(9, 9)
    print("Original Puzzle:")
    for row in np.array(original_grid).astype(int):
        print(row)
    inst = Sudoku_Solver(original_grid)
    grid, count = inst.solve()
    print("Solved Puzzle:")
    for row in np.array(grid):
        print(row)
    print("Calls to Recursive Function:")
    print(count)