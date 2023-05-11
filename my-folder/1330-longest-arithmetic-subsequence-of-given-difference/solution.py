class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        """
        dp is a hashtable, dp[x] is the longest subsequence ending with number x
        """
        dp = {}

        for a in arr:
            if a - d in dp:
               dp[a] = dp[a-d] + 1
            else:
                dp[a]=1

        return max(dp.values())
