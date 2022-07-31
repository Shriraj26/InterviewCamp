"""
In this question u have to set the matrix to zero in the row or column wherever it appears...
Actually, if we have a row and col array to denote wherever zero appears, we can do that and in the end check wherever
it appeared and set the remaining things to zer0.
But it takes O(m+n) space, instead of that, we will do these things in place..we will use one extra variable just for the
element arr[0][0] and use the row = 0 and col 0 from elem 1 onwards of our matrix to denote wherever zero has occurred
"""

row = int(input())
col = int(input())

board = [[int(x) for x in input().split()] for y in range(row)]


def setZeroes():

    rowZero = False
    # get wherever zero occurred
    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                # set row zero to denote that col should be made zero
                board[0][j] = 0

                # set col zero to denote that row should be made zero
                if i > 0:
                    board[i][0] = 0
                else:
                    # set 0,0 to denote that the first row should be made zero
                    rowZero = True


    # do the compute -
    for i in range(1, row):
        for j in range(1, col):
            if board[0][j] == 0 or board[i][0] == 0:
                board[i][j] = 0

    if board[0][0] == 0:
        for i in range(row):
            board[i][0] = 0

    if rowZero:
        for j in range(col):
            board[0][j] = 0




    pass


