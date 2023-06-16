class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = nums.count(0)
        n = len(nums)
        mul = 1
        result = [0] * n
        mul = 1
        
        if zero > 1:
            return result
        if zero == 0:
            for num in nums:
                mul *= num
            for i in range(n):
                result[i] = mul // nums[i]  
        if zero == 1:
            for num in nums:
                if num != 0:
                    mul *= num

            for i in range(n):
                if nums[i] == 0:
                    result[i] = mul 
                else:
                    result[i] = 0 

        return result
