class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        self.heaplen = 0
        
        # Initialize the min-heap with at most k largest elements from nums
        for num in nums:
            self.add(num)
    

    def add(self, val: int) -> int:
        if self.heaplen < self.k:
            self.heap.append(val)
            self.heaplen += 1
            self._heap_up(self.heaplen - 1)

        elif val > self.heap[0]:
            self.heap[0] = val
            self._heap_down(0)

        return self.heap[0]
    def _heap_up(self, i):
        while i > 0:
            par = (i - 1) // 2
            if self.heap[i] < self.heap[par]:
                self.heap[i], self.heap[par] = self.heap[par], self.heap[i]
                i = par
            else:
                break
    def _heap_down(self, i):
        while 2*i+1 < self.heaplen:
            lind = 2*i+1
            rind = 2*i+2
            smallest = lind

                        # Find the smallest child
            if rind < self.heaplen and self.heap[rind] < self.heap[lind]:
                smallest = rind

            if self.heap[i] > self.heap[smallest]:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest

            else:
                break





# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
