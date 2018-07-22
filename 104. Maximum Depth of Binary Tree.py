# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        def __init__(self, root=None):
            self.val = root
            self.left = None
            self.right = None

        def maxDepth(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root is None: return 0
            leftDepth = self.maxDepth(root.left) + 1
            rightDepth = self.maxDepth(root.right) + 1
            return self.maxab(leftDepth, rightDepth)

        def maxab(self,a,b):
            if a > b: return a
            return b