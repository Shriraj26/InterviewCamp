"""
This is the algorithm to visit the graoh by DFS
"""
class GraphNode:

    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def addEdge(self, node):
        self.neighbors.append(node)

class Graph:

    def __init__(self, n):
        self.nodes = {}
        self.visited = {}
        self.length = n


    def dfsVisit(self, node):

        # Mark the node as VISITING
        self.visited[node] = 'VISITING'

        # process the node
        print(node.data)

        # visit its 'UNVISITED' Neighbours
        for neighbor in node.neighbors:
            if self.visited.get(neighbor) is None:
                self.dfsVisit(neighbor)

        # Mark the node as 'VISITED'
        self.visited[node] = 'VISITED'


n = int(input('Enter number of edges '))
edges = [[int(y) for y in input().split()] for x in range(n)]

g = Graph(n)

# add the edges
for node1, node2 in edges:
    node1 = GraphNode(node1)
    node2 = GraphNode(node2)
    node1.addEdge(node2)
    node2.addEdge(node1)
    g.nodes[node1]
    g.nodes.append(node2)

# apply dfs visit from starting node
dec = g.dfsVisit(g.nodes[0])

print(dec)









