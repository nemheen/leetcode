class Solution:
    def tribonacci(self, n: int) -> int:
        zero, one, two, fibn = 0, 1, 1, 0
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        for i in range(3, n+1):
            fibn = zero + one + two
            zero = one
            one = two 
            two = fibn
        return fibn 
        
