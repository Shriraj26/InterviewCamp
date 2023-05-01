"""
INdex of Array = node
Value = its Parent

"""


class Graph:

    def __init__(self, n):
        # initially all the nodes will have same root
        self.rootArr = [i for i in range(n)]
        self.size = n

    # Returns root for a node
    def find(self, node):

        while node != self.rootArr[node]:
            node = self.rootArr[node]

        return node

    def union(self, nodeX, nodeY):
        rootX = self.find(nodeX)
        rootY = self.find(nodeY)

        if rootY != rootX:
            # Change y's root's val to x's root
            self.rootArr[rootY] = rootX

    def connected(self, nodeX, nodeY):
        return self.find(nodeX) == self.find(nodeY)
