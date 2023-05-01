"""
Behold, this is supereme of the supereme!!
This has Union By Rank
And Path Compression!!!

Time Complexity - 
Union Find Constructor - O(n)
Find - O(α(N)) 
Union - O(α(N))
Connected - O(α(N))
α refers to the Inverse Ackermann function. In practice, we assume it's a constant.
In other words, O(α(N)) is regarded as O(1) on average.

Space - O(n) to store rank and rootArr

"""


class UnionFind:

    def __init__(self, size) -> None:
        self.rank = [1] * size
        self.rootArr = [i for i in range(size)]

    def find(self, node):

        if node == self.rootArr[node]:
            return node

        # Get root for this node
        rootNode = self.find(self.rootArr[node])
        # Update the rootArr to include the correct root
        self.rootArr[node] = rootNode
        # return this root
        return rootNode

    def union(self, X, Y):

        # Get roots of X and y
        rootX = self.find(X)
        rootY = self.find(Y)

        if rootX != rootY:

            if self.rank[rootX] > self.rank[rootY]:
                self.rootArr[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.rootArr[rootX] = rootY

            else:
                self.rootArr[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, X, Y):
        return self.find(X) == self.find(Y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
