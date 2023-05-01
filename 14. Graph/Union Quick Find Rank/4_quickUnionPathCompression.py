"""
This is optimized Quick Union and it has optimized find method..
In Quick Union, whenever we call find method, u need to traverse the whole parent 
links till u reach the root.. but u can actually store it in the rootArr
And return it afterwards.. this is DP!!

Time Complexity -
Union Find Constructor - O(n) 
Find - O(log(n))
Union - O(log(n))
Connected - O(log(n))
"""


class UnionFind:

    def __init__(self, size) -> None:
        self.rootArr = [i for i in range(size)]

    def find(self, node):

        if node == self.rootArr[node]:
            return node

        # Find the root for the node. .Therefore in find method, u pass in the root
        # of the node and not just the node!!!!
        root = self.find(self.rootArr[node])
        # Store it in the root Arr
        self.rootArr[node] = root
        # Return this root
        return root

    def union(self, nodeX, nodeY):
        rootX = self.find(nodeX)
        rootY = self.find(nodeY)

        if rootX != rootY:

            if rootY != rootX:
                # Change y's root's val to x's root
                self.rootArr[rootY] = rootX

    def connected(self, nodeX, nodeY):
        return self.find(nodeX) == self.find(nodeY)


uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
