class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, lower, upper):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not is_valid(node.right, val, upper):
                return False
            if not is_valid(node.left, lower, val):
                return False

            return True

        return is_valid(root, float('-inf'), float('inf'))

