class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        i = 0
        for j in range(len(t)):
            if i < n and t[j] == s[i]:
                i += 1
    
        return n == i
