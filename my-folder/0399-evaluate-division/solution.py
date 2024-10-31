from typing import List

class Solution:
    def dfs(self, node: str, dest: str, gr: dict, vis: set, temp: float) -> float:
        if node in vis:
            return -1.0  # Return a flag value if destination not found

        vis.add(node)
        if node == dest:
            return temp  # Found the destination, return the calculated value

        for ne, val in gr[node].items():
            result = self.dfs(ne, dest, gr, vis, temp * val)
            if result != -1.0:  # If a valid result is found, propagate it back up
                return result

        return -1.0  # If no path found, return flag value

    def buildGraph(self, equations: List[List[str]], values: List[float]) -> dict:
        g = {}

        for i in range(len(equations)):
            dd, dr = equations[i]
            val = values[i]

            if dd not in g:
                g[dd] = {}
            if dr not in g:
                g[dr] = {}
            g[dd][dr] = val
            g[dr][dd] = 1.0 / val

        return g
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = self.buildGraph(equations, values)
        
        out = []

        for query in queries:
            dd, dr = query

            if dd not in g or dr not in g:
                out.append(-1.0)
            else:
                visited = set()
                result = self.dfs(dd, dr, g, visited, 1.0)  # Call dfs and get result
                out.append(result)

        return out

