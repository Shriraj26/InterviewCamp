"""
Chekc if the tree is BST or not..
conditions to check-
At a node - whether max of left subtree is less than the current node and then min of right subtree is greater than
the current node, then it is the BST

        6
    4      7
3     5       8
"""
import sys


class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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


def checkBST(root):

    if root is None:
        return -sys.maxsize, sys.maxsize


    leftData = checkBST(root.left)
    rightData = checkBST(root.right)

    # if this constraint fails, then return -1
    if leftData is None or rightData is None:
        return None

    if leftData[0] > root.data or rightData[1] < root.data:
        return None

    currMin = min(leftData[1], rightData[1], root.data)
    currMax = max(leftData[0], rightData[0], root.data)

    return currMax, currMin




# Construct a tree from the input array
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

#printTree(Root)

res = checkBST(Root)
if res is None:
    print('Not a BST')
else:
    print('is a bst')

