class Solution:
    def dfs(self, node, visited, graph):

        if node not in visited:
            visited.add(node)
            for k in graph[node]:
                self.dfs(k, visited, graph)


    def buildG(self, rooms, n):
        g = {}

        for i, keys in enumerate(rooms):
            g[i] = keys
    
        return g

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        g = self.buildG(rooms, n)
        vis = set()

        self.dfs(0, vis, g)
        return n==len(vis)

    
        
