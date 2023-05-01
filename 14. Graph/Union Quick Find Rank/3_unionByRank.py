"""
This is optimized Quick Union, it has optimized union function.
FInd function is same but union function takes note of the rank array
Check the rank of root, if it is greater, connect second tree to first, vice versa
Else if similar rank of both roots, connect second to first and then inc rank 
of first

Time Complexity -
Union Find Constructor - O(n) 
Find - O(log(n))
Union - O(log(n))
Connected - O(log(n))
"""


class UnionFind:

    def __init__(self, size) -> None:
        self.rank = [1] * size
        self.rootArr = [i for i in range(size)]

    def find(self, node):
        while node != self.rootArr[node]:
            node = self.rootArr[node]

        return node

    def union(self, nodeX, nodeY):
        rootX = self.find(nodeX)
        rootY = self.find(nodeY)

        if rootX != rootY:

            # Compare ranks of their roots
            if self.rank[rootX] > self.rank[rootY]:
                # Connect y's root to x's root
                self.rootArr[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.rootArr[rootX] = rootY

            else:
                print('Here ', rootX, rootY, ' for nodex ', nodeX, nodeY)
                self.rootArr[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, nodeX, nodeY):
        return self.find(nodeX) == self.find(nodeY)


uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.rank)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
