"""
This is same as course scheduele but with stack
if there is a cycle, return [],
else return the stack arr
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Construct the graph
        g = {i: [] for i in range(numCourses)}
        for dest, src in prerequisites:
            g[src].append(dest)

        visited = set()
        ancestor = set()
        stack = []

        def topSortHelperAndNoCycle(node):

            visited.add(node)
            ancestor.add(node)

            for neighbor in g[node]:
                if neighbor not in visited:
                    if topSortHelperAndNoCycle(neighbor) == False:
                        return False
                elif neighbor in ancestor:
                    return False

            stack.append(node)
            ancestor.remove(node)
            return True

        for node in g.keys():
            if node not in visited:
                if topSortHelperAndNoCycle(node) == False:
                    return []

        return stack[::-1]
