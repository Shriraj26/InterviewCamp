

class BTNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def printAllPathsToLeaf(root, path, mainPath):

    # base case when we arraive at leaf, print the path and append it to main Path
    if root is None:
        return

    if root.left is None and root.right is None:
        path += str(root.val)
        mainPath.append(path)
    else:
        path += (str(root.val)+'->')

    printAllPathsToLeaf(root.left, path, mainPath)
    printAllPathsToLeaf(root.right, path, mainPath)

    path = path[:-1]

def printTree(root):

    if root is None:
        return

    print(root.val)

    printTree(root.left)
    printTree(root.right)


root1 = BTNode(1)
root2 = BTNode(2)
root3 = BTNode(3)
root4 = BTNode(4)
root5 = BTNode(5)

root1.left = root2
root1.right = root3

root2.left = root4
root2.right = root5


mainPath = []

# printTree(root1)
printAllPathsToLeaf(root1, '', mainPath)
print(mainPath)

