class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret=0
        minimum=prices[0]
        for i in range(len(prices)):
            ret=max(ret, prices[i]-minimum)
            minimum=min(minimum, prices[i])
        return ret
