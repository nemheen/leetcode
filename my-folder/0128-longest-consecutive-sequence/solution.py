class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums=list(set(nums))
        nums.sort()
        res=[]

        maxL = 0
        curL=0
        for n in nums:

            if res and res[-1] == n-1:
                curL += 1
                maxL=max(maxL,curL)
                res.append(n)
            else:

                curL=0
                res.append(n)
        return maxL+1




        


        






