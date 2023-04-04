class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        dir = 0
        res = []

        while top<=bottom and left<=right:
            if dir==0:
                for i in range(left, right+1):
                    res.append(matrix[top][i])
                top=top+1
            elif dir==1:
                for j in range(top, bottom+1):
                    res.append(matrix[j][right])
                right=right-1
            elif dir==2:
                for k in range(right, left-1, -1):
                    res.append(matrix[bottom][k])
                bottom=bottom-1
            elif dir==3:
                for l in range(bottom, top-1, -1):
                    res.append(matrix[l][left])
                left=left+1
            dir=(dir+1)%4
        return res

