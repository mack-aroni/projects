import numpy as np
import warnings


"""
relError(a,b):
helper function to compute relative error of a and b
"""


def relError(a, b):
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        try:
            return np.abs(a-b)/np.max(np.abs(np.array([a, b])))
        except:
            return 0.0


"""
swapRows(M,i,j):
swaps rows i and j of matrix M
works on M in place
"""


def swapRows(M, i, j):
    tmp = M[i].copy()
    M[i] = M[j]
    M[j] = tmp


"""
rowReduce(M,i,j,p):
reduce row j using row i with pivot p in matrix M
works on M in place
"""


def rowReduce(M, i, j, p):
    factor = float(M[j][p] / M[i][p])
    for k in range(len(M[j])):
        if np.isclose(M[j][k], factor * M[i][k]):
            M[j][k] = 0.0
        else:
            M[j][k] = M[j][k] - factor * M[i][k]


"""
rowEchelon(matrix):
returns the row echelon form of matrix using forward elimination
"""


def rowEchelon(matrix):
    M = matrix.copy().astype(float)
    m, n = np.shape(M)
    for i in range(m-1):
        # LNZCol(leftmost non zero) be the position of the leftmost
        # nonzero value in row i or any row below it
        LNZRow = m
        LNZCol = n
        # for each row below row i (including row i)
        for h in range(i, m):
            # search, starting from the left, for the first nonzero
            for k in range(i, n):
                if (M[h][k] != 0.0) and (k < LNZCol):
                    LNZRow = h
                    LNZCol = k
                    break
        # if there is no such position, stop
        if LNZRow == m:
            break
        # if the leftmostNonZeroCol in row i is zero, swap
        # this row with a row below it to make that position
        # nonzero this creates a pivot in that position
        if (LNZRow > i):
            swapRows(M, LNZRow, i)
        # use row reduction operations to create zeros
        # in all positions below the pivot.
        for h in range(i+1, m):
            rowReduce(M, i, h, LNZCol)
    return M


"""
reducedRowEchelon(matrix):
returns the reduced row echelon form of matrix using forward
elimination and backsubstitution
"""


def reducedRowEchelon(matrix):
    M = rowEchelon(matrix)
    # iterates from the end of the matrix to the front
    for i in reversed(range(len(M))):
        # finds the non-zero indexes of the row
        r = np.transpose(np.nonzero(M[i]))
        # if there is a non-zero index which isnt the last index
        if len(r) != 0 and r[0] != len(M[i]) - 1:
            piv = r[0]
            # simplify row
            M[i] = M[i] / M[i][piv]
            # subtract previous rows by the piv row
            for j in range(i):
                rowReduce(M, i, j, piv)
    return M


"""
matrixSolver():
parent function that returns solution
"""


def matrixSolver(matrix):
    RE = rowEchelon(matrix)
    RRE = reducedRowEchelon(RE)
    return (RE, RRE)


if __name__ == "__main__":
    n = int(input("Matrix Height: \n"))
    print("--------------------")
    matrix = [[] for i in range(n)]
    for i in range(n):
        row = input()
        matrix[i] = row.split(" ")
    print("--------------------")
    matrix = np.array(matrix)
    RE, sol = matrixSolver(matrix)
    print("Row Echelon Form \n", RE)
    print("Solution: \n", sol)
