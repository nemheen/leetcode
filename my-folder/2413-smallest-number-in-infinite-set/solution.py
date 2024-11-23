import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.q = []
        self.small = 1

    def popSmallest(self) -> int:
        if self.q:
            return heapq.heappop(self.q)
        self.small += 1
    
        return self.small-1

    def addBack(self, num: int) -> None:
        if self.small > num and num not in self.q:
            heapq.heappush(self.q, num)
            heapify(self.q)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
