"""
THis is exact same as we did in the Tree BFS
1. Declare a queue, visited set
2. Add current node to visited and in queue
3. While queue loop
4. pop from, queue, process it
5. loop neighbors of the node, 
    if not visited, mark visited
    add to the queue
"""
import queue


def bfs(g, v):

    q = queue.Queue()
    visited = set()
    visited.add(v)
    q.put(v)
    while q.qsize():

        curr = q.get()
        print(curr)

        for neighbor in g[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)
