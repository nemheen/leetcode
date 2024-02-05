class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
        res = []
        q = deque([root])
        
        while q:
            qlen = len(q)
            r = None

            for i in range(qlen):
                node = q.popleft()
                if node:
                    r = node
                    q.append(node.left)
                    q.append(node.right)
            if r:
                res.append(r.val)

        return res
