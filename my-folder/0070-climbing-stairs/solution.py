class Solution:
    def climbStairs(self, n: int) -> int:
        df = [0] * (n+1)
        return self.helper(n, df)
    
    def helper(self, n: int, df: List[int]) -> int:
        if n == 0 or n == 1:
            return 1
        
        if df[n] > 1:
            return df[n]
        
        df[n] = self.helper(n-1, df) + self.helper(n-2, df)
        
        return df[n]

