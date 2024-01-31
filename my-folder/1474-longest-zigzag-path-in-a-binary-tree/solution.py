# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root, dir, l):
            nonlocal maxx
            if not root:
                return 0

            maxx = max(maxx, l)

            if dir == 'r':
                dfs(root.left, 'l', l+1)
                dfs(root.right, 'r', 1)

            else:
                dfs(root.left, 'l', 1)
                dfs(root.right, 'r', l+1)

        
        maxx = 0
        dfs(root, 'r', 0)
        dfs(root, 'l', 0)
        
        return maxx
