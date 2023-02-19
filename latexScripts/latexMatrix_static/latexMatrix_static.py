# Ethan Machleder
# latexMatrix_static.py
# takes a rough matrix from input.txt and outputs the
# result as an augmented matrix in latex syntax in output.txt

import numpy as np
import warnings

# global variable that stores the output string
latexString = ""

# compute the relative error of a and b
def relError(a, b):
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        try:
            return np.abs(a-b)/np.max(np.abs(np.array([a, b])))
        except:
            return 0.0

# stage 1 (forward elimination)
# return the row echelon form of B
def forwardElimination(B):
    global latexString
    A = B.copy().astype(float)
    printMatrix(A)
    m, n = np.shape(A)
    for i in range(m-1):
        # let lefmostNonZeroCol be the position of the leftmost 
        # nonzero value in row i or any row below it
        leftmostNonZeroRow = m
        leftmostNonZeroCol = n
        # for each row below row i (including row i)
        for h in range(i, m):
            # search, starting from the left, for the first nonzero
            for k in range(i, n):
                if (A[h][k] != 0.0) and (k < leftmostNonZeroCol):
                    leftmostNonZeroRow = h
                    leftmostNonZeroCol = k
                    break
        # if there is no such position, stop
        if leftmostNonZeroRow == m:
            break
        # if the leftmostNonZeroCol in row i is zero, swap
        # this row with a row below it to make that position
        # nonzero this creates a pivot in that position
        if (leftmostNonZeroRow > i):
            # adds each operation to latexString
            latexString += "swap row {} with row {}, ".format(A,leftmostNonZeroRow)
            swapRows(A, leftmostNonZeroRow, i)
        # use row reduction operations to create zeros
        # in all positions below the pivot.
        for h in range(i+1, m):
            rowReduce(A, i, h, leftmostNonZeroCol)
        # calls printMatrix to show the updated form of the matrix
        printMatrix(A)
    return A

# interchange two rows of A
# operates on A in place
def swapRows(A, i, j):
    tmp = A[i].copy()
    A[i] = A[j]
    A[j] = tmp

# reduce row j using row i with pivot pivot, in matrix A
# operates on A in place
def rowReduce(A, i, j, pivot):
    global latexString
    factor = float(A[j][pivot] / A[i][pivot])
    # adds each operation to latexString    
    latexString += "{} * row {} - row {}, ".format(isInt(factor),i+1,j+1)
    for k in range(len(A[j])):
        if np.isclose(A[j][k], factor * A[i][k]):
            A[j][k] = 0.0
        else:
            A[j][k] = A[j][k] - factor * A[i][k]

# return the reduced row echelon form matrix of B
def backsubstitution(B):
    global latexString
    C = forwardElimination(B)
    # iterates from the end of the matrix to the front
    for i in reversed(range(len(C))):
        # finds the non-zero indexes of the row
        r = np.transpose(np.nonzero(C[i]))
        # if there is a non-zero index which isnt the last index
        if len(r) != 0 and r[0] != len(C[i])-1:
            piv = r[0]
            # if the pivot isnt 1, add the operation to latexString
            if (isInt(C[i][piv]) != 1):
                latexString += "divide row {} by {}, ".format(i+1,isInt(C[i][piv]))
            # simplify row
            C[i] = C[i] / C[i][piv]
            # subtract previous rows by the piv row
            for j in range(i):
                rowReduce(C, i, j, piv)
    # calls printMatrix to show the updated form of the matrix
    printMatrix(C)
    return C

# prints out the current form of the matrix in latex syntax
def printMatrix(A):
    global latexString
    # adds the prefix for the matrix form in latex
    latexString += "\n$$\n\\begin{"+"bmatrix}\n"
    # iterates through the rows
    for row in A:
        # iterates through each index
        for i in range(len(row)):
            # format in latex form, last index has a different form
            if (i == len(row)-1):
                latexString += "{} \\\ \n".format(isInt(row[i]))
            else:
                latexString += "{} & ".format(isInt(row[i]))
    # adds the postfix for the matrix form in latex
    latexString += "\\end{"+"bmatrix}\n$$\n"
    
# returns x as an integer or as a float
def isInt(x):
    if (float(x).is_integer()):
        return int(x)
    return float(x)

# main run loop
def run():
    # take input frmo input.txt as a string
    with open("cs132\latexScripts\latexMatrix_static\input.txt","r") as in_file:
        string = str(in_file.read())
    # remove unecessary symbols
    string = string.replace("&","")
    string = string.replace("\\","")
    # split the string by newlines into a list
    # each split is a raw String row
    string_l = string.split('\n')
    temp_list = []
    # iterates through each index in string_l
    for row in string_l:
        nums = []
        # splits row by " "
        for x in row.split(" "):
            # checks if x is not a number
            # else adds it to nums
            if (isInt(x) != False):
                nums.append(float(x))
        # adds each row of nums onto temp_list
        temp_list.append(nums)
    # forms a numpy matrix from temp_list
    matrix = np.array(temp_list)
    print(matrix)
    # perform backsubstitution on matrix
    backsubstitution(matrix)
    # sends output to output.txt
    with open("cs132\latexScripts\latexMatrix_static\output.txt","w") as out_file:
        out_file.write(latexString)
    in_file.close()
    out_file.close()
run()