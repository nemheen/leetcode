class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        one = []

        for curr in range(lo, hi+1):
            temp = curr
            p = 0
            while temp > 1:
                if temp % 2 == 0:
                    temp //= 2
                else:
                    temp = 3*temp + 1
                p += 1
            heapq.heappush(one, (p, curr))
        
        kth = 0
        while k > 0 and one:
            kth = heapq.heappop(one)
            k -= 1
        return kth[1]
