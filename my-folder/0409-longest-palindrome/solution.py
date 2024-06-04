class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = []
        for letter in s:
            if letter not in ss:
                ss.append(letter)
            else:
                ss.remove(letter)
        if len(ss) != 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)
        
