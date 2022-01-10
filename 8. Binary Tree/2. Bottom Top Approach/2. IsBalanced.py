"""
IsBalanced - At any node, the difference between height of left and right subtrees should be at most 1 and not greater
than that.

Algo -
We return -1 if the tree is not balanced, else we return the height of the Tree, at the end check if we get -1, then,
the tree is not balanced

We will consider a dummy tree as follows -
          1
     2
 4      5    --- this tree is not balanced


"""

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBalanced(root):

    if root is None:
        return 0

    leftHeight = isBalanced(root.left)
    rightHeight = isBalanced(root.right)

    print('Node - ', root.data, ' left height - ',leftHeight, ' right height - ', rightHeight)
    # if either left or right subtrees give -1 as the ans, then we return as -1 as the tree is not balanced
    if leftHeight == -1 or rightHeight == -1:
        return -1

    # if the height diff is greater than 1, return -1
    if abs(leftHeight - rightHeight) > 1:
        print('Here at node ', root.data, leftHeight, rightHeight)
        return -1

    # u reached here it means that tree is balanced at this node, then return the height

    return max(leftHeight, rightHeight) + 1


Root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

Root.left = node2
node2.left = node4
node2.right = node5

#

decision = isBalanced(Root)

if decision == -1:
    print('Tree is not Balanced')
else:
    print('Tree is balanced and Height of the Tree is - ',decision - 1)

