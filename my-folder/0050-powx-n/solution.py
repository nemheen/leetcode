class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = False
        result = 1

        if n == 0:
            return 1
        
        if n < 0:
            negative = True
            n = -n
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n = n // 2
        if negative == True:
            return 1 / result
        else:
            return result
