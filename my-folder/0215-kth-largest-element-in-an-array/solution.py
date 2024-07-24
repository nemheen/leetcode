import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for i in range(k):
            hp.append(nums[i])

        
        heapq.heapify(hp)

        for i in range(k, len(nums)):
            if hp[0] < nums[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, nums[i])


        return hp[0]

        
