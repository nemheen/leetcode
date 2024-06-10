import numpy as np

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hrow, hcol = {}, {}
        n = len(grid)
        k = 0

        for row in grid:
            rowt = tuple(row)
            hrow[rowt] = hrow.get(rowt, 0) + 1


        tgrid = np.transpose(grid)

        for col in tgrid:
            colt = tuple(col)
            hcol[colt] = hcol.get(colt, 0) + 1

        for t, c in hrow.items():
            k += c * hcol.get(t, 0)

        return k


