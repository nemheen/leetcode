class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * n

        for i in range(n):
            if i == 0:
                out[0] = sum(1 for n in nums[1:] if n < nums[0])
            elif i == n-1:
                out[n-1] = sum(1 for n in nums[:n] if n < nums[-1])
            else:
                out[i] = sum(1 for n in nums[:i] if n < nums[i]) + sum(1 for n in nums[i+1:] if n < nums[i])

        return out
        
