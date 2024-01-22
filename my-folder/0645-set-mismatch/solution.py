class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = dict()
        n = len(nums)
        miss, double = 0, 0
        nums = sorted(nums)
        for i in range(n):
            d[i+1] = 0

        for n in nums:
            d[n] += 1
            if d[n] == 2:
                double = n
        for k, v in d.items():
            if v == 0:
                miss = k
        return [double, miss]

