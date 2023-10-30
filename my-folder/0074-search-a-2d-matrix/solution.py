class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1

        
        while row < rows and col > -1:
            curr = matrix[row][col]
            if curr == target:
                return True
            if curr < target:
                row += 1
            else:
                col -= 1
        return False
                


            



