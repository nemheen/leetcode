# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#class Solution:
    #def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
     #   ret = []
     #   if root is None:
     #       return

       # ret += self.postorderTraversal(root.left)
       # ret += self.postorderTraversal(root.right)
      #  ret.append(root.val)
       # return ret#

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if root is None:
            return ret

        ret += self.postorderTraversal(root.left)
        ret += self.postorderTraversal(root.right)
        ret.append(root.val)
        return ret

        
