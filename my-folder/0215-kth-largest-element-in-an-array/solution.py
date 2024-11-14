import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for i in range(len(nums)):

            heapq.heappush(hp, nums[i])
            
            if len(hp) > k:
                heapq.heappop(hp)

        

        return hp[0]

        
