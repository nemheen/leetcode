class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_possible(speed):
            hours_needed = sum(pile // speed + (pile % speed != 0) for pile in piles)
            return hours_needed <= h

        r = max(piles)
        l = 1
        mid = 0

        while l < r:
            mid = (l + r) // 2
            if is_possible(mid):
                r = mid
            else:
                l = mid + 1
        return l
        
