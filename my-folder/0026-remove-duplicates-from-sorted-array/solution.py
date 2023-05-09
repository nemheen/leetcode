class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        # Initialize variables
        i = n - 2
        duplicates = 0
        
        # Iterate over the list from right to left
        while i >= 0:
            if nums[i] == nums[i+1]:
                duplicates += 1
            else:
                duplicates = 0
            if duplicates > 0:
                nums.pop(i)
            i -= 1
        
        return len(nums)

