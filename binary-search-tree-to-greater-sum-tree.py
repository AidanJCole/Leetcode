# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.rInorder(root, 0)
        return root

    def rInorder(self, root, sum):
        if root == None:
            return sum

        if root.right != None:
            sum = self.rInorder(root.right, sum)

        sum += root.val
        root.val = sum

        if root.left != None:
            sum = self.rInorder(root.left, sum)

        return sum