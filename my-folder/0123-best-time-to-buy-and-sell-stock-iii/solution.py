class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        
        # Initialize the buy and sell arrays
        buy = [0] * 3
        sell = [0] * 3
        
        # Base case initialization
        for i in range(3):
            buy[i] = -prices[0]
        
        # Fill the buy and sell arrays dynamically
        for i in range(1, n):
            for j in range(1, 3):
                buy[j] = max(buy[j], sell[j-1] - prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])
        
        return sell[2]

