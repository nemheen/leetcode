class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        
        # Base case initialization
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] ) #selling
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i] ) #buying
        return dp[n-1][0]

