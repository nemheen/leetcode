class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = sorted(nums)
        mapping = {}
        out = []
        plus = 0
        for i in range(len(num)):
            if num[i] not in mapping:
                mapping[num[i]] = i
        
        return [mapping[j] for j in nums]
