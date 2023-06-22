class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        opnum = 0
        dic = {}
        for num in nums:
            d = k - num
            if dic.get(d, 0) > 0:
                opnum += 1
                dic[d] -= 1
            else:
                dic[num] = dic.get(num, 0) + 1
        return opnum

