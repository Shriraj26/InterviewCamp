"""
Solved Here...
https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
"""


def detectCycleUndirected(g, v):

    visited = set()

    def detectCycleUndirected(node, parent):

        visited.add(node)

        for neighbor in g[node]:

            # Check if neighbor not visited, then call recursively
            if neighbor not in visited:
                if detectCycleUndirected(neighbor, node):
                    return True

            # This means that there is an edge from the node
            # To neighbor that is already visited and it is not a
            # a parent.. then it is a cycle
            elif parent != neighbor:
                return True

        return False

    for node in g.keys():
        if node not in visited:
            if detectCycleUndirected(node, -1):
                return True

    return False
