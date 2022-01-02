"""
SudokuSolver:​ Given a Sudoku board, find a solution. The board can have some squares filledout already.
You have to fill the rest of the squares.(Rules of Sudoku are as follows: In each column, row and 3 x 3 square,
you cannothave duplicate numbers. Also, only numbers 1-9 are allowed.)
"""

# Take inputs -
mat = [[int(x) for x in input().split()] for y in range(9)]

# For every element, we will have a matrix for checking if that elem can be placed into a row
row = [[None for x in range(10)] for y in range(9)]

# For every element, we will have a matrix for checking if that elem can be placed into a col
col = [[None for x in range(10)] for y in range(9)]

# For every element, we will have a matrix for checking if that elem can be placed into a box of 3*3
box = [[None for x in range(10)] for y in range(9)]


# Helper Funcitons that we will need -

# place an item into the board
def place(i, j, num):

    if canPlace(i, j, num) is False:
        return False

    row[i][num] = True
    col[j][num] = True
    boxNumber = findBoxNumber(i,j)
    box[boxNumber][num] = True

    return True


# Remove a number from a sudoku board... If next i and next j fails, then we need to call this function
def removeElem(i, j, num):
    row[i][num] = False
    col[j][num] = False
    boxNum = findBoxNumber(i, j)
    box[boxNum][num] = False

# Check Whether I can place an element into a position or not?
def canPlace(i, j, num):


    # Check if number is already placed in row, then it cannot be placed again, return False
    if row[i][num]:
        return False

    # Check if number is already placed in Col, then it cannot be placed again, return False
    if col[j][num]:
        return False

    # Check if it can be placed in a box
    boxNum = findBoxNumber(i, j)

    if box[boxNum][num]:

        return False

    return True

# Find 3*3 box number for a particular i,j
def findBoxNumber(i, j):

    return (i//3)*3 + (j//3)

# find the next element to place in to the board after i,j
def nextElem(i, j):

    if j == 8:
        return i+1, 0

    return i, j+1

# Print matrix helper function
def printMat(mat):

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end = ' ')
        print()



# Initialize the row, col and box matrices, here we need to add the existing numbers to the board
def placeExistingElements():

    for i in range(9):
        for j in range(9):
            if mat[i][j] != 0:
                place(i, j, mat[i][j])



# Solve the sudoku
def sudokuSolver(i, j):
    # 5. Base case if we reach the i where i == 9, then we return True
    if i == 9:
        return True

    # 5. Base case If the current element is already filled, then proceed to next i,j
    if mat[i][j] != 0:
        next_i, next_j = nextElem(i, j)
        return sudokuSolver(next_i, next_j)

    # 2. Splits = check from 1 to 9 if it can be placed into the position
    for num in range(1, 10):

        # check if u can place the elem -
        if canPlace(i, j,num):

            # Initially place the elem
            place(i, j, num)
            mat[i][j] = num

            # get next i and j to place
            next_i, next_j = nextElem(i, j)

            # Call for next and next j to place
            if sudokuSolver(next_i, next_j):
                return True

            # If u reach here it means that we cannot place this number at i,j thus we remove it
            removeElem(i, j, num)
            mat[i][j] = 0

    # If u reach here it means that u could not place the elem, thus return False
    return False


placeExistingElements()
print(sudokuSolver(0, 0))
printMat(mat)



