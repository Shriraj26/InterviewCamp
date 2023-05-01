"""
This is a question of detecting cycle in directed graph...
If there is a cycle, u cannot finish all the courses..
Thats it
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build a graph
        g = {i: [] for i in range(numCourses)}
        for dest, src in prerequisites:
            g[src].append(dest)

        # Declare visited and ancestor
        visited = set()
        ancestor = set()

        # DFS recurse is Cycle for directed
        def isCycleDirected(node):

            visited.add(node)
            ancestor.add(node)

            # Loop neighbors
            for neighbor in g[node]:
                if neighbor in ancestor:
                    return True
                elif neighbor not in visited:
                    if isCycleDirected(neighbor):
                        return True

            ancestor.remove(node)
            return False

        # Call this function for all the vertices in the graph
        for node in g.keys():
            if node not in visited:
                if isCycleDirected(node):
                    return False

        return True
