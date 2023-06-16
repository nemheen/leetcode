class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
       
        min_val = second_min_val = float('inf')
        
        for i in range(len(nums)):
            if nums[i] <= min_val:
                min_val = nums[i]
            elif nums[i] <= second_min_val:
                second_min_val = nums[i]
            else:
                return True
        
        return False

