# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.path = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left < 0:
                left = 0
        
            if right < 0:
                right = 0

            self.path = max(self.path, node.val+left+right)
            return node.val + max(left, right)

       
        dfs(root)
        return self.path
