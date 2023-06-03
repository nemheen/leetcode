class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        #create graph
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        #return max time needed for each employee.
        def helper(node):
            ans = 0
            for c in graph[node]:
                ans = max(ans, informTime[node] + helper(c))
            return ans
            
        return helper(headID)

        
