class Solution:
     def numSquares(self, n: int) -> int:
        # Nice Approach 2nd fastest
        # if n <= 0:
        #     return 0
        #
        # cnt_perfect_square = [0]
        #
        # while len(cnt_perfect_square) <= n:
        #     m = len(cnt_perfect_square)
        #     cnt_square = sys.maxsize
        #     for i in range(1, int(math.sqrt(m)) + 1):
        #         cnt_square = min(cnt_square, cnt_perfect_square[m - i * i] + 1)
        #     cnt_perfect_square.append(cnt_square)
        # return cnt_perfect_square[n]

        # We can Use Langrage's 4 Square theorem to do this in very efficient manner
        def is_perfect_square(n):
            square_root = int(math.sqrt(n))
            return square_root**2 == n
        
        cpy_n = n
        if is_perfect_square(n):
            return 1
        # 4^k(8m + 7) if in this way a num. can be represented then it's a sum of 4 square nums.
        while n & 3 == 0:    # divisible by 4
            n >>= 2           # divide by 4
        if n & 7 == 7:       # n & 7 ---> n % 8 == 0  and n & 7 == 7 means n % 8 == 7
            return 4
        n = cpy_n
        for i in range(1, int(math.sqrt(n)) + 1):
            if is_perfect_square(n - i*i):
                return 2
        return 3
        
