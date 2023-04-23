class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        maxx, start = 0, 0
        for i, c in enumerate(s):
            while c in sset:
                sset.remove(s[start])
                start += 1
            sset.add(c)
            maxx = max(maxx, i-start+1)
        return maxx
