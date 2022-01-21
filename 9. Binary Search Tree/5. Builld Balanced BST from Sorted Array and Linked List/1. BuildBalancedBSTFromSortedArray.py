"""
Given a sorted array, build a balanced Binary Search Tree with the elements of the array.

1. find the mid of the array
2. make it root
3. get left subtree from recursively callign the fn to elements to the left of arr...
4. get right subtree from recursively callign the fn to elements to the right of arr...
5. Connect the left and right subtrees
"""


class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printTree(root):
    q = []
    q.append(root)

    while len(q) > 0:

        node = q[0]

        if node.left is not None:
            q.append(node.left)

        if node.right is not None:
            q.append(node.right)

        print(node.data)
        q.pop(0)

def constructBalancedBST(arr,start, end):


    if start > end or start < 0 or end >= len(arr):
        return None

    mid = start + (end - start)//2


    root = BSTNode(arr[mid])

    leftSubtree = constructBalancedBST(arr, start, mid-1)
    rightSubtree = constructBalancedBST(arr, mid+1, end)

    root.left = leftSubtree
    root.right = rightSubtree

    return root


arr = [int(x) for x in input().split()]

root = constructBalancedBST(arr, 0, len(arr)-1)

printTree(root)
