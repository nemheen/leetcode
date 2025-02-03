class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # a - increase, b - decrease, c - max len answer
        a = b = c = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                a += 1
                b = 1
               
            elif nums[i] < nums[i-1]:
                b += 1
                a = 1
                print(a, b)
            else:
                a = b = 1
            
            c = max(c, max(a, b))

        return c
