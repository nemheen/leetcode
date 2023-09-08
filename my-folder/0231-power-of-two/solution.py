class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        elif n<=0:
            return False
        while n > 2:
            n /= 2
        if n%2==0:
            return True
        return False

