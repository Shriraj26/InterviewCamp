"""
In this case, we dont have any parent pointer.. Therefore we need to use the bottom up approach...
The algo is like this, for finding out LCA among nodes A and B
1. If u encounter a node that is either A or B, then return that node
2. If u get null then return null
3. A node if gets node A from left subtree and gets node B from right subtree, then only it is the LCA of both the nodes!!!
4. Else if nothing is returned, then we return None

We will consider a dummy tree as follows -
          1
     2         3
 4      5   6      7   ---- Height will be 2


"""

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowestCommonAncestor(root, A, B):

    if root is None:
        return None

    # Our condition - if u get a node that is A or B, then return that node
    if root == A or root == B:
        return root

    # call left and right subtrees!!!
    leftLCA = lowestCommonAncestor(root.left, A, B)
    rightLCA = lowestCommonAncestor(root.right, A, B)

    # This is the condition for LCA, if left and right both return non null things, then the current node is the LCA
    if leftLCA is not None and rightLCA is not None:
        return root

    # else if either of them is None, return the non None wala or return None
    if leftLCA is not None:
        return leftLCA
    elif rightLCA is not None:
        return rightLCA
    return None



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


print('Finding LCA of nodes - 6 and 7')
print(lowestCommonAncestor(Root, node6, node7).data)

print('Finding LCA of nodes - 3 and 5')
print(lowestCommonAncestor(Root, node3, node5).data)

