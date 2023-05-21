class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        def sol(left, right):
            res = []
            if left > right:
                return [None]

            for root in range(left, right+1):
                leftTrees = sol(left, root-1)
                rightTrees = sol(root+1, right)

                for leftNode in leftTrees:
                    for rightNode in rightTrees:
                        node = TreeNode(root)
                        node.left = leftNode
                        node.right = rightNode
                        res.append(node)

            return res

        return sol(1, n)

