class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ssum = 0
        for i in range(k):
            ssum += nums[i]

        most = ssum
        i = 0
        j = k

        while j < len(nums):
            ssum -= nums[i]
            ssum += nums[j]
            most = max(ssum, most)
            i += 1
            j += 1
        return most / k

