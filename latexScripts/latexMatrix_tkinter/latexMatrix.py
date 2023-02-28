from tkinter import *
from tkinter import messagebox
import numpy as np
import warnings

root = Tk()
root.title('latexMatrix')
root.resizable(False,False)

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
    C = B.copy().astype(float)
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
    
# checks if x in a num if true returns as an integer or float
# else returns False
def isInt(x):
    try:
        if (float(x).is_integer()):
            return int(x)
        return float(x)
    except ValueError:
        return False
    
def run():
    global latexString
    latexString = ""
    string = str(in_text.get("1.0", "end-1c"))
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
            if (x == "0"):
                nums.append(float(x))
            elif (isInt(x) != False):
                nums.append(float(x))
        # adds each row of nums onto temp_list
        # skips any empty rows
        if (len(nums) > 0):
            temp_list.append(nums)
    # forms a numpy matrix from temp_list
    # attempts to create a matrix from temp_list
    # an error means an invalid input was inserted
    print(temp_list) # input testing
    try:
        matrix = np.array(temp_list)
        # performs forward elimination on the matrix
        matrix_new = forwardElimination(matrix)
        # perform backsubstitution on matrix
        backsubstitution(matrix_new)
        # displays output on the output screen
        out_text.configure(state=NORMAL)
        out_text.delete("1.0", "end-1c")
        out_text.insert("1.0",latexString)
        out_text.configure(state=DISABLED)
    except Exception:
        messagebox.showerror("Error", "Error: Invalid Input")
    

# adds the output to the users clipboard
def copy():
    out_text.configure(state=NORMAL)
    root.clipboard_clear()
    root.clipboard_append(out_text.get('1.0', 'end-1c'))
    out_text.configure(state=DISABLED)
    
def clear():
    in_text.delete('1.0', 'end-1c')
    out_text.configure(state=NORMAL)
    out_text.delete('1.0', 'end-1c')
    out_text.configure(state=DISABLED)


# Create the first text box and its scrollbar
in_text = Text(root, height=20, width=30)
scroll_in = Scrollbar(root, command=in_text.yview)
in_text.config(yscrollcommand=scroll_in.set)

# Create the second text box and its scrollbar
out_text = Text(root, height=20, width=30, state=DISABLED)
scroll_out = Scrollbar(root, command=out_text.yview)
out_text.config(yscrollcommand=scroll_out.set)

# Pack the text boxes and scrollbars in the main window
in_text.pack(side=LEFT)
scroll_in.pack(side=LEFT, fill=Y)
out_text.pack(side=LEFT)
scroll_out.pack(side=LEFT, fill=Y)

# button to solve the matrix given in the input and display to the output
button_run = Button(root, text="Solve",command=run).pack()

# button to clear both the input and output screens
button_clear = Button(root, text="Clear",command=clear).pack()

# button to copy output screen to clipboard
button_copy = Button(root, text="Copy",command=copy).pack()

root.mainloop()
