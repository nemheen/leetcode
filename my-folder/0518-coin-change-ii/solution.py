class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp =[ [0]*(n+1) for i in range(amount+1) ]
        dp[0] = [1]*(n+1)

        for a in range(1, amount+1):
            for i in range(n-1, -1, -1):
                dp[a][i] = dp[a][i+1]
                if a-coins[i] >= 0:
                    dp[a][i] += dp [a-coins[i]] [i]
        return dp[amount][0]




