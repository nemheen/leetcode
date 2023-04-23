class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [x.lower() for x in s if x.isalnum()]
        return a == a[::-1]

