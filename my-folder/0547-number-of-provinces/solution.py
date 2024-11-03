from typing import List, Dict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        # Step 1: Build the graph as an adjacency list
        graph = self.buildGraph(isConnected, n)
        
        # Step 2: DFS to count connected components
        visited = [False] * n
        ans = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(i, visited, graph)
                ans += 1
        
        return ans

    def buildGraph(self, isConnected: List[List[int]], n: int) -> Dict[int, List[int]]:
        graph = {i: [] for i in range(n)}  # Initialize an empty adjacency list for each node
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:  # Skip self-loops
                    graph[i].append(j)  # Add j as a neighbor of i
        return graph

    def dfs(self, node: int, visited: List[bool], graph: Dict[int, List[int]]):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, graph)

