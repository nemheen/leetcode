class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
      n = len(nums)
      dp = {}
      res, len_ans = 0, 0

      for i in range(n-1, -1, -1):
        maxlen, maxcount = 1, 1
        for j in range(i+1, n):
          if nums[i] < nums[j]:
            length, count = dp[j]
            if length +1 > maxlen:
              maxlen, maxcount = length+1, count
            elif length +1 == maxlen:
              maxcount += count
        if maxlen > len_ans:
          len_ans, res = maxlen, maxcount
        elif len_ans == maxlen:
          res += maxcount
        dp[i] = [maxlen, maxcount] 

      return res

