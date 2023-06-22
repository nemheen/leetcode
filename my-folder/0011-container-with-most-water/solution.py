class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r , res = 0, len(height) - 1, 0

        while l <= r:
            area = min(height[r], height[l])*(r-l)
            res = max(res, area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return res
