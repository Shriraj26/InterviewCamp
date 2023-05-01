"""
Index of array is the node and its value is its root and not its parent!!
Therefore the find operation is O(1), and union operation in this case is O(n).
For find, just return the value at its index.
FOr uniom of 2 nodes, decide a root and apply it to the second root.
Convert all the indices that have second root to first root.
"""


class Graph:

    def __init__(self, n):
        # initially all the nodes will have same root
        self.rootArr = [i for i in range(n)]
        self.size = n

    def find(self, node):
        return self.rootArr[node]

    def union(self, nodeX, nodeY):
        rootX = self.find(nodeX)
        rootY = self.find(nodeY)

        if rootX != rootY:
            for i in range(self.size):
                if self.rootArr[i] == rootY:
                    self.rootArr[i] = rootX

    def connected(self, nodeX, nodeY):
        return self.find(nodeX) == self.find(nodeY)
