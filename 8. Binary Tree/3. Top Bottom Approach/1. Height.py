"""
From root, keep on adding the height at its children, and maxHeight will be a array of single length as we have to pass it
by reference, thus maxHeight will update once we reach the ultra depth!!

We will consider a dummy tree as follows -
                      1
                 2         3
            4      5
        6            7
    8                  9

"""
import sys


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

def heightTopDown(root, parentHeight, maxHeight):

    if root is None:
        return

    currentHeight = parentHeight + 1

    root.height = currentHeight
    maxHeight[0] = max(maxHeight[0], currentHeight)

    heightTopDown(root.left, currentHeight, maxHeight)
    heightTopDown(root.right, currentHeight, maxHeight)



Root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

Root.left = node2
Root.right = node3
node2.left = node4
node2.right = node5

node4.left = node6
node6.left = node8

node5.right = node7
node7.right = node9


maxHeight = [-sys.maxsize]
heightTopDown(Root, 0, maxHeight)
print('Max Height obtainied is- ', maxHeight[0]-1)

print(node8.height)
print(node7.height)
print(node3.height)
print(node5.height)