"""
Bas ek hi cheez hai bhai
Neighbor's level != Current Node's level
"""

import queue


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # Construct graph
        g = {}
        for i, edges in enumerate(graph):
            g[i] = edges

        # Visited and queue, level
        visited = set()
        q = queue.Queue()

        def bfs(node):
            visited.add(node)
            q.put(node)
            level = {node: 0}

            while q.qsize():
                node = q.get()
                for neighbor in g[node]:

                    if neighbor not in visited:
                        level[neighbor] = level.get(node, 0) + 1
                        q.put(neighbor)
                        visited.add(neighbor)

                    elif level.get(neighbor, 0) == level.get(node, 0):
                        return False

        for node in g.keys():
            if node not in visited:
                if bfs(node) == False:
                    return False

        return True
