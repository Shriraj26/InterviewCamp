"""
In this case, we have to use Stack to visit the Tree in the Inorder manner, remember the fact that, in order to get result
in stack , u have to insert in reverse as it is a lsast in first out... Therefore,
1. Normal Inorder has - left, root and right, we will insert in this manner now - right, root, left
2. We will mantain a visited array for all the members in the Tree becosz, we dont want to visit the node again...

Algo is this -
1. Push the root into Stack
2. while stack not empty, pop the node
3. If popped node was visited, print it
4. else, mark it as visited, push its left and right children if not None

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
visited = {}


def initVisited(root):
    if root is None:
        return

    visited[root] = False
    initVisited(root.left)
    initVisited(root.right)


def inOrderUsingIteration(root):
    # Push the root first
    stk.append(root)

    # Now loop till stack is not Empty
    while len(stk) > 0:

        # pop a node
        node = stk.pop()

        # if the node was visited, print it
        if visited[node]:
            print(node.data, end=' ')
        else:

            # else mark it as true
            visited[node] = True

            # push its right child
            if node.right is not None:
                stk.append(node.right)

            # push the node now that has now been marked as visited
            stk.append(node)

            # push the left child
            if node.left is not None:
                stk.append(node.left)


# This will initialize the visited dictionary for the node
initVisited(Root)

# Call the inorder using Iteration method.
inOrderUsingIteration(Root)
