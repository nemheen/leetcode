class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i in counter.keys():
            if counter[i] >= 2:
                return True
        return False

            
