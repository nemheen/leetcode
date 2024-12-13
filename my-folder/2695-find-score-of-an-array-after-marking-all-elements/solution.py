class Solution:
    def findScore(self, nums: List[int]) -> int:
        sc = 0
        n = len(nums)
        mark = [False] * n
        h = [(nums[i], i) for i in range(n)]
        heapq.heapify(h)

        while h:
            val, ind = heapq.heappop(h)
            if mark[ind]:
                continue
            
            sc += val

            mark[ind] = True

            if ind > 0:
                mark[ind-1] = True
            if ind < n-1:
                mark[ind+1] = True
        return sc


