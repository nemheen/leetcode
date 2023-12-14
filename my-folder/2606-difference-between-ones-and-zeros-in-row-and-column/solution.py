import numpy as np


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        grid = np.array(grid)

        rows_ones = np.sum(grid == 1, axis=1)
        cols_ones = np.sum(grid == 1, axis=0)
        rows_zeros = np.sum(grid == 0, axis=1)
        cols_zeros = np.sum(grid == 0, axis=0)

        diff = (rows_ones[:, np.newaxis] + cols_ones) - (rows_zeros[:, np.newaxis] + cols_zeros)

        return list(diff)

