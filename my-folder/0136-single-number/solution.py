from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       a=Counter(nums)
       res = list([k for k,v in a.items() if v ==1])
       for i in res:
           return i
