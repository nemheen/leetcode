class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res, prefixSum, h = 0, 0, []

        for a, b in sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True):
            prefixSum += a
            heappush(h, a)

            if len(h) == k:
                res = max(res, prefixSum * b)
                prefixSum -= heappop(h)

        return res
