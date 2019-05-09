# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def rInsert(self, root, x):
        if root == None:
            return TreeNode(x)
        elif x > root.val:
            node = TreeNode(x)
            node.left = root
            return node
        else:
            root.right = self.rInsert(root.right, x)
            return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        root = None

        for x in nums:
            root = self.rInsert(root, x)

        return root