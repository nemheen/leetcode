class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        if not s or s[0] == '0':
            return 0
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            v = int(s[i-1:i])
            if v >= 1 and v < 10:
                dp[i] += dp[i-1]
            v = int(s[i-2:i])
            if v > 9 and v <= 26:
                dp[i] += dp[i-2]

        return dp[-1]

