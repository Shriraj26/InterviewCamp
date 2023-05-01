"""
In this we have an array that stores, index as destination and the value as 
source, we apply bfs and keep on storing the nodes 
in the result...

"""
from queue import Queue


def bfs(src, dest, g):

    visited = set()
    predecessor = [-1] * len(g)
    q = Queue()
    visited.add(src)
    q.put(src)

    while q.qsize():

        src = q.get()

        # loop neighbors
        for neighbor in g[src]:

            if neighbor not in visited:
                q.put(neighbor)
                predecessor[neighbor] = src
                visited.add(neighbor)

                if neighbor == dest:
                    break

    # Check if no path till destination
    if predecessor[dest] == -1:
        return []

    path = [dest]
    iterator = dest
    while predecessor[iterator] != -1:
        iterator = predecessor[iterator]
        path.append(iterator)

    return path[::-1]
