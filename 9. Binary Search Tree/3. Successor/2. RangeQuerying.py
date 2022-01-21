"""
Given a Binary Search Tree, find all the elements in the range [A..B], both A and B inclusive.
For example, if we are looking for nodes in the range [5,8] in the following tree:

        6
    4      7
3     5       8

Ans - 5 6 7 8

"""

class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rangeQuery(root, range1, range2):
    if root is None:
        return

    if root.data < range1:
        # go right
        rangeQuery(root.right, range1, range2)
        pass
    if root.data > range2:
        # go left
        pass
    if root.data >= range1 and root.data <= range2:
        # call left with range2 = root.data
        rangeQuery(root.left, range1, root.data)

        print(root.data, end = ' ')

        # call right with range1 = root.data
        rangeQuery(root.right, root.data, range2)




Root = BSTNode(6)

node4 = BSTNode(4)
node7 = BSTNode(7)

node3 = BSTNode(3)
node5 = BSTNode(5)
node8 = BSTNode(8)

Root.left = node4
Root.right = node7

node4.left = node3
node4.right = node5

node7.right = node8


rangeQuery(Root, 5, 8)
print()
rangeQuery(Root, 3, 6)
print()
rangeQuery(Root, 7, 8)
print()
rangeQuery(Root, 10, 12)





