class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums = sorted(list(set(nums)))
        one, two = 0, 0

        for i in range(len(nums)):
            earned = nums[i]*counter[nums[i]]

            if i>0 and nums[i] == nums[i-1]+1:
                temp = two
                two = max(earned + one, two)
                one = temp

            else:
                temp = two
                two = earned + two
                one = temp
        return two



