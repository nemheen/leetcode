class Solution:
    def finalPrices(self, p: List[int]) -> List[int]:
       
        ans = []
        n = len(p)
        

        for i in range(n):
            dis = 0
            for j in range(i+1, n):
                if p[j] <= p[i]:
                    dis = p[j]
                    break

            ans.append(p[i]-dis)
    
        return ans
        
