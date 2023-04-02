class Solution:
   
    def isHappy(self, n: int) -> bool:
        return self.solve(n, [])

    def solve(self, n: int, track: List[int]) -> bool:
        if n==1:
            return True
        res=sum(int(i)**2 for i in str(n))
        if res in track:
            return False
        else:
            track.append(res)
        return self.solve(res, track)
    
        
        
            

        

