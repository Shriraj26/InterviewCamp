"""
in this case we dont have to use a visited marker, this method off implementation will do the trick

Algo =
1. take a node , first it will be root
2. in loop , check if the node is not None or stack is not Empty
3. Then if node is not None, append it and assign the node to its left child
4. if at any point node gets None, then pop the top of the stack
5. print its value, then push its right child

We will consider a dummy tree as follows -
          1
     2         3
 4      5   6      7

"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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

stk = []


def inOrderUsingIterationNotVisited(root):
    node = root

    while node is not None or len(stk) > 0:

        if node is not None:
            stk.append(node)
            node = node.left

        else:
            node = stk.pop()
            print(node.data, end=' ')
            node = node.right


# Call the inorder using Iteration method without using visited array or hashtable.
inOrderUsingIterationNotVisited(Root)
