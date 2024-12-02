from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], st: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        q = deque([(st[0], st[1], 0)])

        maze[st[0]][st[1]] = '+'

        vis = set()
        vis.add((st[0], st[1]))

        while q:
            row, col, s = q.popleft() #row, col, steps

            for dr, dc in dirs:
                r, c = row + dr, col + dc

                if 0 <= r < n and 0 <= c < m and maze[r][c]=='.' and (r, c) not in vis:
                    if r == 0 or r == n-1 or c == 0 or c == m-1:
                        return s + 1

                    vis.add((r, c))

                    q.append((r, c, s+1))
            

        return -1
        
