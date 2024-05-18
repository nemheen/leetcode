class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        def helper(i, visited, isConnected):
            visited[i] = True
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    helper(j, visited, isConnected)
        
        
        visited = [False] * n
        ans = 0
        for i in range(n):
            if visited[i] == False:
                helper(i, visited, isConnected)
                ans += 1
        
        return ans

