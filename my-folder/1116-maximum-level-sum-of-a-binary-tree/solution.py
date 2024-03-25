# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        lvl = 0
        maxl = 0
        maxv = float('-inf')

        q = deque([root])

        while q:
            lvl += 1
            qlen = len(q)
            ssum = 0

            for i in range(qlen):
                
                node = q.popleft()
                ssum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                

            if ssum > maxv:
                maxl = lvl
                maxv = ssum
    
        return maxl

