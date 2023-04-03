# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Create an empty stack and push the root node...
        bag = [root]
        # Create an array list to store the solution result...
        sol = []
        # Loop till stack is empty...
        while bag:
            # Pop a node from the stack...
            node = bag.pop()
            if node:
                sol.append(node.val)
                # Append the right child of the popped node into the stack
                bag.append(node.right)
                # Push the left child of the popped node into the stack
                bag.append(node.left)
        return sol      # Return the solution list...

     
