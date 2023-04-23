class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        curr = []
        curr.append(1)

        prev = self.getRow(rowIndex-1)
        for i in range (rowIndex-1):
            curr.append(prev[i]+prev[i+1])

        curr.append(1)
        return curr
