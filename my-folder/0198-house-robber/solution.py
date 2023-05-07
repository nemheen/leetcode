class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        robbed = [0]*n 
        robbed[0] = nums[0]
        robbed[1] = nums[1]
        for i in range(2, n):
            if i > 2:
                robbed[i] = nums[i] + max(robbed[i-2], robbed[i-3])
            else:
                robbed[i] = nums[i] + robbed[i-2]

        return max(robbed[-1], robbed[-2])

