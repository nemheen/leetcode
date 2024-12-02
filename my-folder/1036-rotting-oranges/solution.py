class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        q = deque()
        fresh = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0
    
        vis = set()

        while q:
            row, col, t = q.popleft() #row, col, time

            for dr, dc in dirs:
                r, c = row + dr, col + dc

                if 0 <= r < n and 0 <= c < m and grid[r][c]==1 and (r, c) not in vis:
                    fresh -= 1
                    vis.add((r, c))

                    q.append((r, c, t+1))
            time = t if t > time else time

        return time if fresh==0 else -1
        
