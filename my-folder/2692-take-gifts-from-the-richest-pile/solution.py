import math 
class Solution:
    def pickGifts(self, g: List[int], k: int) -> int:
       

        j = -1
        for i in range(k):
            g = sorted(g)
            g[j] = int(math.sqrt(g[j]))

        s = sum(g)
        return s
