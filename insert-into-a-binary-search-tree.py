# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        if root == None:
            return TreeNode(val)
        else:
            temp = root
            prev = None
            while temp is not None:
                if val > temp.val:
                    prev = temp
                    temp = temp.right
                else:
                    prev = temp
                    temp = temp.left
            node = TreeNode(val)
            if val > prev.val:
                prev.right = node
                return root
            else:
                prev.left = node
                return root