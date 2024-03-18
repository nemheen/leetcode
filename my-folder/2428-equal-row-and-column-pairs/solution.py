import numpy as np
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid = np.array(grid)
        trans = grid.transpose()

        row_counts = {}
        col_counts = {}

        # Count occurrences of each row
        for row in grid:
            row_tuple = tuple(row)
            row_counts[row_tuple] = row_counts.get(row_tuple, 0) + 1

        # Count occurrences of each column
        for col in trans:
            col_tuple = tuple(col)
            col_counts[col_tuple] = col_counts.get(col_tuple, 0) + 1

        # Count pairs with equal row and column counts
        equal_pairs = 0
        for row_tuple, row_count in row_counts.items():
            equal_pairs += row_count * col_counts.get(row_tuple, 0)

        return equal_pairs

