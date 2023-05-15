class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        if n < m:
            nums1, nums2, m, n = nums2, nums1, n, m
        dp = [0]*(m+1)
        for i in range(n-1, -1, -1):
            prev = 0
            for j in range(m-1, -1, -1):
                current = dp[j]
                if nums1[i] == nums2[j]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(current, dp[j+1])
                prev = current
        return dp[0]

