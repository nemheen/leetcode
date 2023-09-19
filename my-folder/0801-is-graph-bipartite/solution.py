from collections import defaultdict

class Solution:
    def isBipartite(self, graph):


        def dfs(vertex, group):
            # Assign the current vertex to the specified group
            groups[vertex] = group

            for neighbor in graph[vertex]:
                if neighbor not in groups:
                    # If the neighbor is not assigned to a group, assign it to the opposite group
                    if not dfs(neighbor, 1 - group):
                        return False
                elif groups[neighbor] == group:
                    # If the neighbor is in the same group as the current vertex, the graph is not bipartite
                    return False

            return True

        # Initialize a dictionary to keep track of vertex groups (0 or 1)
        groups = {}

        # Iterate through all vertices in the graph
        for vertex in range(len(graph)):
            if vertex not in groups:
                # Start DFS from unassigned vertices with group 0
                if not dfs(vertex, 0):
                    return False

        return True

