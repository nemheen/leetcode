class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}

        for i in range(1, len(nums)):
          for j in range(i):
            d = nums[i] - nums[j]
            if (j,d) in dp:
              dp[i, d] = dp[j, d] + 1
            else:
              dp[i, d] = 2
            

        return max(dp.values())
    
