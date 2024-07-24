class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
    
        # Iterate through each element in the array
        for num in arr:
            # Push the current element with the negative distance to max-heap
            heapq.heappush(max_heap, (-abs(num - x), -num))
            
            # If the heap size exceeds k, remove the farthest element
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # Extract elements from the heap and sort them
        result = [-num for _, num in max_heap]
        result.sort()
        
        return result


            

        
        
        
