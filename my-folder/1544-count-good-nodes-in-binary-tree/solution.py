class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val):
            if not root:
                return 0

            good_nodes = 0
            if root.val >= max_val:
                good_nodes += 1
                max_val = root.val

            good_nodes += dfs(root.left, max_val)
            good_nodes += dfs(root.right, max_val)

            return good_nodes

        return dfs(root, float('-inf'))
