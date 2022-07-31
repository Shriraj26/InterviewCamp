""""""
"""
This is the algorithm to visit the graoh by BFS -
# Create a queue
# add root node to it
# mark the node as visiting
while q is not Empty:

    # pop from queue -- pop 0

    # process the node, print it

    # put all of its unvisited neighbors in the queue and mark them visiting (unvisited = visited[node] is None)

    # mark the curr as visited
"""
class GraphNode:

    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def addEdge(self, node):
        self.neighbors.append(node)

class Graph:

    def __init__(self, nodesList):
        self.nodes = nodesList
        self.visited = {}


    def bfsVisit(self, node):

        q = [node]
        # mark the node as visiting
        self.visited[node] = 'VISITING'
        while len(q) > 0:

            curr = q.pop(0)

            # Process the node, just print it
            print(curr.data)

            # loop all the neighbors
            for n in curr.neighbors:
                if self.visited.get(n) is None:
                    # mark the neighbor as visiting
                    self.visited[n] = 'VISITING'
                    q.append(n)

            # Finally mark it as visited
            self.visited[curr] = 'VISITED'

node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)

node1.addEdge(node2)
node1.addEdge(node3)

node2.addEdge(node4)
node3.addEdge(node4)

g = Graph([node1, node2, node3, node4])

g.bfsVisit(node1)









