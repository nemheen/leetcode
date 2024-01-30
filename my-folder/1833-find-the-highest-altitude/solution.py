class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        curr = 0
        for i in range(len(gain)):
            curr += gain[i]
            h = max(curr, h)
        return h
        
