class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
                
            l = i + 1
            r = n - 1
            k = - num
            
            while l < r:
                curr = nums[l] + nums[r]
                if curr == k:
                    result.append([num, nums[l], nums[r]])

                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                  
                elif curr < k:
                    l += 1
                else:
                    r -= 1
        
        return result

