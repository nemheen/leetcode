class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one, two = 0, 1
        
        while numbers[one] + numbers[two] != target:
            if numbers[one] + numbers[two] < target:
                one+=1
                two += 1
            else:
                one -= 1
        return [one+1, two+1]


