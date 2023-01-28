class Solution:
    def longestPalindrome(self, s: str) -> int:
        res=0
        counter = Counter(s)
        y=0
        for k,v in counter.items():
            if v%2==0:
                res += v
                
            else:
                res += v - 1
                y=y+1
     
        if y>0:
            return res+1
        else:
            return res

