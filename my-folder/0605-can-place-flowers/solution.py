class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        i = 0
        while i < len(f):
            if n == 0:
                return True

            if f[i] == 0:
                if (i==0 or f[i-1]==0) and (i==len(f)-1 or f[i+1]==0):
                    f[i] == 1
                    i += 2
                    n -= 1
                else:
                    i += 1

            else:
                i += 1
        return n==0
