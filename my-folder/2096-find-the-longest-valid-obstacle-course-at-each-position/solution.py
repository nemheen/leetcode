class Solution:
    def longestObstacleCourseAtEachPosition(self, obs: List[int]) -> List[int]:
        dp = list()
        ans = list()
        for ob in obs:
            if not dp or ob >= dp[-1]:
                dp.append(ob)
                ans.append(len(dp))
            else:
                pos = self.binary(dp, ob)
                dp[pos] = ob
                ans.append(pos + 1)
        return ans


    def binary(self, dp: List[int], target: int) -> int:
        l, r = 0, len(dp)-1
        while(l<r):
            mid = (l+r)//2
            if dp[mid] <= target:
               l = mid + 1
            else:
                r = mid
        return l

