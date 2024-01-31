# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root, sum, arr, res):

            if not root:
                return False
            
            arr.append(root.val)
            if not root.left and not root.right:
                if sum == root.val:
                    res.append(list(arr))
                    

            dfs(root.left, sum - root.val, arr, res)
            dfs(root.right, sum - root.val, arr, res)

            arr.pop()
           

        dfs(root, targetSum, [], res)
        return res
