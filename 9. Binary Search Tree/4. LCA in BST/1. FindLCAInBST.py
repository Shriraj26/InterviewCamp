"""
Given two nodes A and B in a Binary Search Tree, find the lowest common ancestor. (You can assume both nodes exist in the tree)
        6
    4      7
3     5       8

The diff between LCA in Tree and LCA in BST is that - in Tree, we were going both left and right as we didnt knew
what values the Tree had as they were not in sorted manner.. But now in BST, we know that sorted thing exists so
we can take a decision as to where to go... In case of BST, theere are 2 cases -
1. current node is less than both the given nodes,  node ..... elem1, elem2... in this case, we have to go right
2. current node is greater than both the nodes,   elem1, elem2 ,,,, node  in this case, we have to go left
3. if current node is between both the nodes -
    this will cover 2 cases -
    1.    3
        1   5   .. if we need to find lca of 1 anf 5, the LCA is 3

    3.    6
        5   ... here if we need to find lca of 6 and 5, it will be the node 6 itself, in this case, if we encounter node like
            this where 6 fits in the range 5 to 6 and it is also the node itself, then we return the node
"""


class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findLCA(root, node1, node2):

    curr = root
    while curr is not None:
        if curr.data < node1.data and curr.data < node2.data:
            # go right
            curr = curr.right
        elif curr.data> node1.data and curr.data > node2.data:
            # go left
            curr = curr.left
        else:
            return curr


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

print('LCA of 3 and 7 ',findLCA(Root, node3, node7).data)
print('LCA of 7 and 8 ',findLCA(Root, node7, node8).data)
print('LCA of 3 and 5 ',findLCA(Root, node3, node5).data)

