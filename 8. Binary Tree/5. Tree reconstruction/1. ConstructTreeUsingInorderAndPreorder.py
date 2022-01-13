"""
If u have only preorder and postorder, u cannot construct tree, as in inorder, the left of the node is the left subtree and
in the right u get the right subtree,
Now, based on either pre-order or post-order, u can determine what is the root of this subtrees and construct the entire tree
through recursion...
The idea is this -
1. Get the root through preorder, first elem of the traversal will be the root itself..
2. Now search in inorder this root, towards the left of the root will be the left subtree,
    towards right of the root will be the right subtree
3. Find right subtree in the pre-order traversal, first elem will be the root of right subtree, same for the left as well
4. connect the subtrees to the root as well and then return

Example -
        4
    2       6
1     3   5     7

Inorder - 1 2 3 4 5 6 7
Pre-rder - 4 2 1 3 6 5 7

4 is the root of the tree
Find 4 in inorder, left of 4 will be the left subtree, right will be right subtree - 1 2 3 .... 4 .... 5 6 7
Now get the roots 2 and 6 from left and right subtrees by recursively calling the function and giving them arrays 1 2 3, and
5 6 7
Connect them to the root and return the root
"""


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


print('Enter inorder Array - ')
inOrderArr = [int(x) for x in input().split()]
print('Enter preorder Array - ')
preOrderArr = [int(x) for x in input().split()]

# Create a hashmap so that the finding of nodes in inorder and preorder becomes easy and in O(1) time
inOrderMap = {}
for i in range(len(inOrderArr)):
    inOrderMap[inOrderArr[i]] = i


def constructBinaryTree(inArr, preArr):
    if len(preArr) == 0 or len(inOrderArr) == 0:
        return None

    # Gwt the root from the preorder Arr, the first node will be the root node
    root = TreeNode(preArr[0])
    index = None
    # find the index where the root exists in inorder
    for i in range(len(inArr)):
        if inArr[i] == root.data:
            index = i

    print('index and value - is - ', index, root.data)
    inorderLeft = inArr[0: index]
    inorderRight = inArr[index + 1:]
    print('Inorder Left and Right - ', inorderLeft, inorderRight)

    preorderLeft = preArr[1: index + 1]
    preorderRight = preArr[index + 1:]
    print('PreOrder Left and Right - ', preorderLeft, preorderRight)

    root.left = constructBinaryTree(inorderLeft, preorderLeft)
    root.right = constructBinaryTree(inorderRight, preorderRight)

    return root


def printTreeLevelWise(root):
    # add root to queue
    q = []
    q.append(root)

    while len(q) > 0:

        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

        print(node.data, end=' ')


root = constructBinaryTree(inOrderArr, preOrderArr)

printTreeLevelWise(root)


# 9 3 15 20 7
# 3 9 20 15 7