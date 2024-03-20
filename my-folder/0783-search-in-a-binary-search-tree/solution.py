# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        

        if root is None:
            return None

        if root.val == target:
            return root
        elif root.val > target:
            return self.searchBST(root.left, target)
        else:
            return self.searchBST(root.right, target)

        
        
        
