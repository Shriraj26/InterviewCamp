"""
Given a Binary Search Tree that can contain duplicates, find the first occurrence of the number X.
The first occurrence is the first node that we will encounter in an in-order traversal.

The algo is easy an we use record and move on technique -
1. initialize a root node.
2. if node is greater than the given elem, go left,
3. if node is smaller than the given elem, go right,
4. if node is equal, then record the node and then again go left... by this way, if there still exists duplicates, we can
find it in its left...

        4
    2       6
1      4  5    7
"""

class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findFirstOccurrence(root, elem):

    res = None

    while root is not None:

        if root.data > elem:
            root = root.left
        elif root.data < elem:
            root = root.right
        else:
            res = root
            root = root.left

    return res


def printTree(root):

    q = []
    q.append(root)

    while len(q) > 0:

        node = q.pop(0)
        print(node.data)
        if node.left is not None:
            q.append(node.left)

        if node.right is not None:
            q.append(node.right)



Root = BSTNode(4)
node2 = BSTNode(2)
node6 = BSTNode(6)
node1 = BSTNode(1)
node4 = BSTNode(4)
node5 = BSTNode(5)
node7 = BSTNode(7)

Root.left = node2
Root.right = node6

node2.left = node1
node2.right = node4
node6.left = node5
node6.right = node7

print('Enter the elem u wnat to search first occurrence - ')
X = int(input())

#printTree(Root)
print('Node that has first occurrence ',findFirstOccurrence(Root, X))
