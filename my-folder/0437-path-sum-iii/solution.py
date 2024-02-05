class Solution:
    def pathSum(self, root, targetSum):
        def dfs(node, targetSum):
            if not node:
                return 0

            count = int(node.val==targetSum)
            count += dfs(node.right, targetSum - node.val)
            count += dfs(node.left, targetSum - node.val)
            return count

        if not root:
            return 0

        total_count = dfs(root, targetSum)
        total_count += self.pathSum(root.left, targetSum)
        total_count += self.pathSum(root.right, targetSum)

        return total_count
