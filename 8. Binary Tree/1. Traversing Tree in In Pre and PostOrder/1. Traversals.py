"""
Inorder - Left, Root, Right -- Remember BST - sorted order -- inorder
PreOrder - Root, Left, Right
PostOrder - Left, Right, Root

We will consider a dummy tree as follows -
          1
     2         3
 4      5   6      7


Note the space Complexity for this thing is - O(h) where h is the height of the tree...
This due to the recursion stack taking the space
"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.data, end=' ')
    inOrder(root.right)


def preOrder(root):
    if root is None:
        return

    print(root.data, end=' ')
    inOrder(root.left)
    inOrder(root.right)


def postOrder(root):
    if root is None:
        return

    inOrder(root.left)
    inOrder(root.right)
    print(root.data, end=' ')



Root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

Root.left = node2
Root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

print('Inorder - ')
inOrder(Root)
print()

print('Preorder - ')
preOrder(Root)
print()

print('Postorder - ')
postOrder(Root)

