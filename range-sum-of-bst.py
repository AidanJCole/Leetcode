# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root == None:
            return None

        return self.rSearch(root, L, R)

    def rSearch(self, node, L, R):
        sum = 0
        if node == None:
            return sum;
        if node.val >= L and node.val <= R:
            sum += node.val
        if node.val >= L:
            sum += self.rSearch(node.left, L, R)
        if node.val <= R:
            sum += self.rSearch(node.right, L, R)
        return sum    