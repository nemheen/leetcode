class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        rem = n - 1
        pos = 1

        while rem:
            if not (x & pos):
                res |= (rem & 1) * pos
                rem >>= 1
            pos <<= 1
        return res
