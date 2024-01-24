class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        ones = res = 0
        while l <= r and r < len(nums):
            if nums[r] == 1:
                ones += 1
                r+=1
            elif nums[r] == 0:
                r = l = r + 1
                res = max(res, ones)
                ones = 0
        res = max(res, ones)
        return res
        
