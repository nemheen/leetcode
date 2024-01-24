class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        maxx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            while k < zeros:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            maxx = max(maxx, i - l + 1)
        return maxx
                
