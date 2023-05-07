class Solution:
    def fib(self, n: int) -> int:
        one,two, fib = 0, 1, 0
        if n==0 or n==1:
            return n
        for i in range(2, n+1):
            fib = one + two
            one = two
            two = fib
        return fib 

