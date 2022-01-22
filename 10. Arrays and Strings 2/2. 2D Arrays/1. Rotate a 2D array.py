"""
Rotate a 2d arrays clockwise or anti clockwise
First take a transform
1. For anti-clockwise, do a up-down shift
2. For clockwise, do a right-left shift
See the func for more details...
"""

n, m = input().split()
n = int(n)
m = int(m)
arr =[[int(x) for x in input().split()] for y in range(n)]

# this step is common for both the cases, after it wither clockwise or anticlockwise
def transposeArray():

    i = 0
    while i < n:
        j = i
        while j < n:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

            j += 1
        i += 1
        print()

# For anti-clockwise
def antiClockWise():

    # 1 4 7       3 6 9
    # 2 5 8  =>   2 5 8
    # 3 6 9       1 4 7

    j = 0
    while j < n:
        start = 0
        end = n-1
        while start < end:
            arr[start][j], arr[end][j] = arr[end][j], arr[start][j]

            start += 1
            end -= 1
        j += 1


# For clockwise
def clockWise():
    # swap the elem at i, j with i, n-j that is -
    # 1 4 7         7 4 6
    # 2 5 8   =>    8 5 2
    # 3 6 9         9 6 3
    for i in range(len(arr)):

        start = 0
        end = n-1
        while start < end:
            arr[i][start], arr[i][end] = arr[i][end], arr[i][start]
            start += 1
            end -= 1

def printArr():

    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end = ' ')
        print()


transposeArray()
# transFormColsForAntiClockWise()
clockWise()
printArr()


