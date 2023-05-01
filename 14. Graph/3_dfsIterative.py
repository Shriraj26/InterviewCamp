"""


"""


def dfsIterative(g, node):

    visited = set()
    stack = [node]

    while stack:

        curr = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node)

        for neighbor in g[node]:
            if neighbor not in visited:
                stack.append(neighbor)
