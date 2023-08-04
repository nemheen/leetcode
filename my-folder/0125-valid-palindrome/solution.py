class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        punctuations = '''!()-[]{};:'`"\,<>./?@#$%^&*_~'''
        result = "".join([c.lower() for c in s if c not in punctuations])

        l, r = 0, len(result) - 1

        while l < r:
            if result[l] != result[r]:
                return False
            l += 1
            r -= 1
        return True

        

