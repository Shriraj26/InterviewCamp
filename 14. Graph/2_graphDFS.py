"""
Declare visited
Mark node as visited
Process the node
Loop through its neighbors
    if not visited, call recursively
"""
# Function to return a list containing the DFS traversal of the graph.


def dfsOfGraph(self, V, adj):
    # code here

    # Build the graph
    g = {}
    for i, neigh in enumerate(adj):
        g[i] = neigh

    visited = set()
    result = []

    def dfs(node):

        visited.add(node)
        result.append(node)
        for neighbor in g[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(0)
    return result
