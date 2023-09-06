class Solution:
    def maximumCount(self, nums):
        pos, neg = 0, 0
        n = len(nums)
        l, r = 0, n-1
        if nums[-1] < 0 or nums[0] > 0:
            return n

        for i in range(n):
            if nums[i] < 0:
                neg += 1
            if nums[i] == 0:
                continue
            elif nums[i] > 0:
                pos += 1
                
        return pos if pos > neg else neg

