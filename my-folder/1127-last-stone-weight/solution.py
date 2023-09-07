from sortedcontainers import SortedList

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = SortedList(stones)
        while len(s) > 1:
            y = s.pop()
            x = s.pop()
            if x != y:
                s.add(y-x)
        if s:
            return s[0]
        return 0


