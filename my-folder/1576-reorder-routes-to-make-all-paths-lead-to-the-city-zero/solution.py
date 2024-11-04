class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        # Build the graph with directed edges only (no reverse graph needed)
        for u, v in connections:
            graph[u].append((v, True))  # True indicates that the edge is in the original direction
            graph[v].append((u, False)) # False indicates this is a reverse connection back to u

        def dfs(node):
            vis.add(node)
            reversals = 0

            # Traverse all connections of the current node
            for neighbor, is_forward in graph[node]:
                if neighbor not in vis:
                    # If it's a forward edge, count it as a reversal
                    if is_forward:
                        reversals += 1
                    # Continue DFS on the neighbor
                    reversals += dfs(neighbor)
            
            return reversals

        vis = set()
        return dfs(0)

