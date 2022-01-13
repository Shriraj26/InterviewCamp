"""
From root, keep on adding the height at its children, and maxHeight will be a array of single length as we have to pass it
by reference, thus maxHeight will update once we reach the ultra depth!!

When u are done with explorng, u need to pop the node, why? this is the classic case of backtracking, when we exit a node,
the array will still have its data, for ex - when u come at node 8, then array will have data like - 1 2 4 6 8
now in order to explore path 1 2 5 7 9, the array has to remove the node 8 right!!! thus we remove the node and progress!!

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

def pathsTopDown(root, arr):

    if root is None:
        return

    # append the data to the stack
    arr.append(root.data)

    # if u reach the child leaf, then print the array
    if root.left is None and root.right is None:
        print(arr)

    # Explore the left subtree
    pathsTopDown(root.left, arr)

    # Explore the right subtree
    pathsTopDown(root.right, arr)

    # After u have done exploring, pop from the stack!!!
    arr.pop()


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


arr  = []
pathsTopDown(Root, arr)


