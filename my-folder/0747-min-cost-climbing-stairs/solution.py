class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c0, c1=cost[0], cost[1]
        for i in range(2, len(cost)):
            c0, c1=c1, min(c0, c1)+cost[i]
        return min(c0, c1)
