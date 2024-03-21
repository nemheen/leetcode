class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = [0] * (n+1)
        while n > 0:
            curr = n
            count = 0
            while curr:
                count += curr & 1
                curr >>= 1
            ans[n] = count
            n -= 1
        return ans
