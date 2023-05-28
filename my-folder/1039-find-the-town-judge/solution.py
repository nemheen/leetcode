class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if len(trust) < n-1:
            return -1
        counter = {i: 0 for i in range(1, n+1)}
        for t in trust:
            counter[t[0]] -= 1
            counter[t[1]] += 1
        for i in range(1, n+1):
            if counter[i] == n-1:
                return i

        return -1




