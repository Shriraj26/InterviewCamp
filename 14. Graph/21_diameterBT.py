# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The diameter is returned one extra, as we include nodes but we need only edges...
# Remember, left height, right height, and left diameter, right diameter, thats
# it!!! And thode se conditions ...
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # This returns height and diameter
        def diaHelper(root):

            if root is None:
                return 0, 0

            lh, ld = diaHelper(root.left)
            rh, rd = diaHelper(root.right)

            currentHeight = max(lh, rh) + 1
            currentDiameter = 0

            if ld == 0 and rd == 0:
                currentDiameter = 1

            # means that exclude left and right diameter, and root se
            # diameter jayega!!
            elif lh+rh >= max(ld, rd):
                currentDiameter = lh + rh + 1

            # means left ya right ka max lele bhai
            else:
                currentDiameter = max(ld, rd)

            return currentHeight, currentDiameter

        return diaHelper(root)[1] - 1
