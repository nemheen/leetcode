import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:       
        h = []
        for pair in points:
            dis = math.sqrt((pair[0]*pair[0])+(pair[1]*pair[1]))
            
            heapq.heappush(h, (-dis, pair))
            if len(h) > k:
                heapq.heappop(h)

            
        return [pair for _, pair in h]



