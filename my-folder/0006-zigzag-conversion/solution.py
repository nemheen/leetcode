class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        ans = ""
        if numRows >= n or numRows == 1:
            return s
        for i in range(numRows):
            j = i
            while j < n:
                ans += s[j]
                if i != 0 and i != numRows - 1:
                    next_j = j + (numRows - i - 1) * 2
                    if next_j < n:
                        ans += s[next_j]
                j += (numRows - 1) * 2
        return ans

