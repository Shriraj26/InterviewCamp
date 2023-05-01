"""
DFS and in the end, push the element in the stack
Print the stack in reverse...
Only possible in Directed Acyclic Graph
"""


def topSort(g, v):

    visited = set()
    stack = []

    def topSortHelper(node):

        visited.add(node)
        for neighbor in g[node]:
            if neighbor not in visited:
                topSortHelper(neighbor)

        stack.append(node)

    topSortHelper(v)

    print(stack[::-1])
