class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        l = 0
        maxx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            maxx = max(maxx, i - l + 1)
        return maxx - 1

        
