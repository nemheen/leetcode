class Solution:
    def reverseVowels(self, s: str) -> str:
        l = []
        res = ""
        m = ['a','e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in s:
            if i in m:
                l.append(i)

        for j in s:
            if j in m:
                res += l[-1]
                l.pop(-1)
            else:
                res += j
        return res

