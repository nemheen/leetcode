class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        minn = min(n, m)
        ans = ""
        for i in range(minn):
          ans += word1[i]
          ans += word2[i]
        if n > m:
          ans += word1[minn::]
        else:
          ans += word2[minn::]
        return ans            
