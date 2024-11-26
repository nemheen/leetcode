class Solution:
    def totalCost(self, costs: List[int], k: int, a: int) -> int:
        hone, htwo, res = [], [], 0
        i, j = 0, len(costs)-1

        while k > 0:
            while len(hone) < a and i <= j:
                heappush(hone, costs[i])
                i += 1
            while len(htwo) < a and i <= j:
                heappush(htwo, costs[j])
                j -= 1

            x = hone[0] if hone else float('inf') 
            y = htwo[0] if htwo else float('inf') 


            if x <= y:
                res += x
                heapq.heappop(hone)
            else:
                res += y
                heapq.heappop(htwo)

            k -= 1

        return res
            



        
