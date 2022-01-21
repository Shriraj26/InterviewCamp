"""
Find the in-order successor of a given node in a BST.
In this case, the in-order successor is the next node in the inorder traversal in the BST.

There are 2 cases to look for
1. If the node has right child, then ans is the leftmost child of the right subtree
2. else, if the node has no right child.
    1. if current val is greater than the record that node, then go left
    2. else if current val is less than the node, then go right
    3. if current is equal to the node, then return....

In this way, in step 2, we record the parent that is the first right ancestor of the node.
In step 1, we just print the left most elem of the right child

Time complexity - O(h)


        6
    4      7
3     5       8

"""

class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def successorOfaNodeBST(root, nodeToFind):

    if nodeToFind.right is not None:

        inOrdSuccessor = nodeToFind.right
        while inOrdSuccessor.left is not None:
            inOrdSuccessor = inOrdSuccessor.left
        return inOrdSuccessor
    else:
        res = None
        curr = root

        while curr is not None:

            if curr.data < nodeToFind.data:
                curr = curr.right
            elif curr.data > nodeToFind.data:
                res = curr
                curr = curr.left
            else:
                break


        return res

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


print('INorder successor of node 6 - ', successorOfaNodeBST(Root, Root).data)
print('INorder successor of node 5 - ', successorOfaNodeBST(Root, node5).data)
print('INorder successor of node 4 - ', successorOfaNodeBST(Root, node4).data)
print('INorder successor of node 8 - ', successorOfaNodeBST(Root, node8))



