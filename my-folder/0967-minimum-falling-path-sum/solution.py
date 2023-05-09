class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

       
        for i in range(1, n):
            for j in range(0, m):
                if j == 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1])
                elif j == (m-1):
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j])
                else:
                    matrix[i][j] += min( matrix[i-1][j-1], min( matrix[i-1][j], matrix[i-1][j+1] ) )
        mini = matrix[n-1][0]
        for k in range(0, m):
            mini = min(mini, matrix[n-1][k])
        return mini


