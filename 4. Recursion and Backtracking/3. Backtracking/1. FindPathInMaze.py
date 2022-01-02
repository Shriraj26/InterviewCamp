"""
You are given a 2D array that represents a maze. It can have 2 values - 0 and 1. 1 represents a wall and 0 represents a
path. The objective of the maze is to reach the bottom right corner, or A[A.length-1][A.length-1]. You start from A[0][0]
and can only go in 4 directions - up, down, left or right. Find if a path exists.

Here we follow 5 steps -
1. Core Idea = For every i,j that we are on, check if there is a path till end
2. Splits - Where can we go => top, bottom, right and left
3. Collection/Convergence => If any direction gives result as True, then we return True
4. Memoization -> For Cycle, we check if node has been marked VISITING, and To check if the node cannot have
    path ahead till end, we mark it as PATH_NOT_FOUND
5. Base Cases -
    1. Check if array is not going out of bounds
    2. If we encounter a '1' value or a Wall at any i,j --> return False
    3. Check if we reached Finally
    4. Check if the current node that we are visiting is not in VISITING state(cycle) or not PATH_NOT_FOUND(no path further from this
        point) ... Then return False

"""

m = int(input('Enter number of rows - '))
n = int(input('Enter number of columns - '))
mat = [[int(x) for x in input().split()] for y in range(m)]
memo = [[None for x in range(n)] for y in range(m)]


def outOfBounds(i, j):
    if i >= m or j >= n or i < 0 or j < 0:
        return True


def findPathInMaze(i, j):
    # 1. Check if array is out of bounds
    if outOfBounds(i, j):
        return False

    # 2. Check if current i,j is 1
    if mat[i][j] == 1:
        return False

    # 3. Check if we already reached
    if i == m - 1 and j == n - 1:
        return True

    # 4. Check if we dont encounter a cycle
    if memo[i][j] == 'VISITING':
        return False

    # 5. Check if there is no PATH_NOT_FOUND from that node...
    if memo[i][j] == 'PATH_NOT_FOUND':
        return False

    # Mark the current node as visiting
    memo[i][j] = 'VISITING'

    # Find pairs for the node
    pairs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    # print(pairs)
    # Loop through all the pairs and check if any path exists for a pair
    for pair in pairs:
        if findPathInMaze(pair[0], pair[1]):
            return True

    # At last if we are here it means that we still did not get any oath yet, so we mark the node as PATH_NOT_FOUND
    memo[i][j] = 'PATH_NOT_FOUND'

    # FINALLY, RETURN FALSE
    return False


print(findPathInMaze(0, 0))
