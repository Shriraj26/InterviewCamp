"""
There are 4 cases -

1. if root is none, height is 0 and diameter is 0
2. if ld == 0 or rd == 0, then diameter is 1
3. if lh + rh < ld or lh + rh < rd,  then diameter is max(ld, rd)
4. if lh + rh >= ld or lh + rh >= rd,  then diameter is lh + rh + 1


"""


"""
Height is the maximum number of edges between the root and the leaf node
In this approach, we iterate from bottom to top and increment the height along the way, Why we need this, becoz at any point
of time, a node requires data from left and right subtrees, therefore, the data of left and right subtrees should be
calculated before!! Therefore, we go from bottom to top and then get the result

Algo -
At any point, node checks that height is max of height from left, right child and adds 1 to it as it is a level above them.
And then returns this height
when root is Null, we return 0 so when there is a node that is a leaf node, it's height becomes 1 so final height
is actually 1 more than the actual height, therefore we subtract 1 at last

We will consider a dummy tree as follows -
                      1
                 2         3
            4      5             
        6            7
    8                  9
 

"""

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameter(root):

    # 1.
    if root is None:
        return 0, 0

    lh, ld = diameter(root.left)
    rh, rd = diameter(root.right)

    currentHeight = max(lh, rh) + 1
    currDiameter = 0

    # 2.
    if lh == 0 or rh == 0:
        currDiameter = 1

    # 3.
    elif lh + rh < ld or lh + rh < rd:
        currDiameter = max(ld, rd)

    # 4.
    elif lh + rh >= ld or lh + rh >= rd:
        currDiameter = lh + rh + 1


    return currentHeight, currDiameter

Root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

Root.left = node2
Root.right = node3
node2.left = node4
node2.right = node5

node4.left = node6
node6.left = node8

node5.right = node7
node7.right = node9

TreeHeight, Trediameter = diameter(Root)

print('Diameter of the Tree is - ', Trediameter - 1)

