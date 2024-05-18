class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph, rev_graph = defaultdict(list), defaultdict(list)
        
        for u, v in connections:
            graph[u].append(v)
            rev_graph[v].append(u)

        def dfs(node):
            visited.add(node)
            k = 0

            for neighbor in graph[node]:
                if neighbor not in visited:
                    k += 1
                    k += dfs(neighbor)

            for neighbor in rev_graph[node]:
                if neighbor not in visited:
                    k += dfs(neighbor)
            
            return k
        
        visited = set()
        return dfs(0)


        
