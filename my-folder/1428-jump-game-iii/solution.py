
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()

        def dfs(pos):
            if pos < 0 or pos >= n or pos in visited:
                return False
            visited.add(pos)

            if arr[pos] == 0:
                return True
            return dfs(pos - arr[pos]) or  dfs(pos + arr[pos])
        

        return dfs(start)

