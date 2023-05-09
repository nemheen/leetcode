class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        t = s[::-1]
        dp = [[0 for j in range(n+1)] for i in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if t[i] == s[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
