class Solution:
    def getMaximumXor(self, nums: List[int], n: int) -> List[int]:
        total = 0

        for num in nums:
            total ^= num

        max_k = (1 << n) - 1

        ans = []
        for i in range(len(nums)):
            ans.append(total ^ max_k)

            total ^= nums[-1]

            nums.pop()
        return ans
            
