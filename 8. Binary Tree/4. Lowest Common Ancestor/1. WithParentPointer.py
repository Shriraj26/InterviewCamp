"""

We have a parent pointer of every child node, thus child has reference to its parent...
Thus what we can do is, find the height of the child nodes,
1. If they are on same height, and are equal, then it is the LCA
2. if they are on same height but not equal, then call their parent nodes until they are not equal, at last they
    will be equal and thus it will bt the LCA
3. if they are on diff height, then call parent node of the node whose height is more and then follow steps 1 and 2

We will consider a dummy tree as follows -
          1
     2         3
 4      5   6      7   ---- Height will be 2


"""
maxHeight = [0]
class TreeNode:

    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 0

def heightTopDown(root, parentHeight, maxHeight):

    if root is None:
        return

    currentHeight = parentHeight + 1

    root.height = currentHeight
    maxHeight[0] = max(maxHeight[0], currentHeight)

    heightTopDown(root.left, currentHeight, maxHeight)
    heightTopDown(root.right, currentHeight, maxHeight)



def recurseTillSameHeight(A, heightA, B, heightB):

    # Here A height is more than B, then we go upwards A's Parent

    while heightA != heightB:
        print('A was - ', A.data)
        A = A.parent
        print('A became - ',A.data)
        heightA -= 1

    print('Now at - ', A.data, B.data)
    return A, B

def recurseTillSameNode(A, B):

    if A is None or B is None:
        return None

    if A == B:
        return A

    return recurseTillSameNode(A.parent, B.parent)

def getParentAtSameHeight(A, B, root):

    heightTopDown(root, 0, maxHeight)

    print('Height of ', A.data,' is - ', A.height, ' height of ',B.data, ' is ',B.height)

    LCA = None

    if A == B:
        LCA = A

    if A.height > B.height:
        A, B = recurseTillSameHeight(A, A.height, B, B.height)
    else:
        A, B = recurseTillSameHeight(B, B.height, A, A.height)

    print(A.data, B.data)

    LCA = recurseTillSameNode(A, B)

    print('LCA is ',LCA.data)



Root = TreeNode(1, None)
node2 = TreeNode(2, Root)
node3 = TreeNode(3, Root)
node4 = TreeNode(4, node2)
node5 = TreeNode(5, node2)
node6 = TreeNode(6, node3)
node7 = TreeNode(7, node3)


Root.left = node2
Root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7


getParentAtSameHeight(node2, Root, Root)