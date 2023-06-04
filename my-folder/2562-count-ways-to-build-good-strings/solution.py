class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = {}

        def helper(lenght):
            if lenght > high:
                return 0
            if lenght in dp:
                return dp[lenght]

            dp[lenght] = 1 if lenght >= low else 0
            dp[lenght] += helper(lenght+zero) + helper(lenght+one)
            return dp[lenght] % mod

        return helper(0)

