# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if not root:
            return true;
        return self.isSame(root.left, root.right)
    def isSame(self, leftroot, rightroot):
        if not leftroot  and not rightroot:
            return True
        if not leftroot  or not rightroot:
            return False
        if leftroot.val != rightroot.val:
            return False
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)
