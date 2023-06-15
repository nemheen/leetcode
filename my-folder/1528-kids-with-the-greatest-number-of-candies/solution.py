class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        most = max(candies)
        for i in range(len(candies)):
            if extraCandies + candies[i] >= most:
                result[i] = True
        return result
