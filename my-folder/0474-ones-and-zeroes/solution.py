class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize a 2D DP array
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for s in strs:
            ones, zeros = 0, 0
            for i in range(0, len(s)):
                if s[i] == '1':
                    ones += 1
                elif s[i] == '0':
                    zeros += 1
            
            # Update the DP array
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        
        return dp[m][n]

