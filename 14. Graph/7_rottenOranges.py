"""
This is khatarnaak BFS!! in this we start the bfs from multiple sources...
Put all the nodes into the queue along with inital depth 0
Mark them as visited
Then normal bfs algo but now, you will also keep track of the depth,
get the depth from popping the node from grid,
inc it and pass it to children in the queue
"""

from queue import Queue


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # init the values
        q = Queue()
        visited = set()
        depth = 0
        m, n = len(grid), len(grid[0])

        # Add the rotten oranges to the queue and mark them visited
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.put((i, j, 0))
                    visited.add((i, j))

        # in range
        def inRange(row, col):
            if 0 <= row < m and 0 <= col < n:
                return True

        while q.qsize():

            row, col, depth = q.get()
            paths = [[row+1, col], [row - 1, col], [row, col-1], [row, col+1]]

            # top, bottom, left, right
            for i, j in paths:
                if inRange(i, j) and (i, j) not in visited and grid[i][j] == 1:
                    visited.add((i, j))
                    q.put((i, j, depth+1))

        # Check if all the matrix doesnt have any ones left that is not visited
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    return -1

        return depth
