from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        row_map = {}
        n = len(grid)

        # Count the frequency of each row
        for row in grid:
            row_str = tuple(row)
            row_map[row_str] = row_map.get(row_str, 0) + 1

        # Check each column
        for j in range(n):
            column = [grid[i][j] for i in range(n)]
            column_str = tuple(column)

            # If the column is equal to any row, increment the count
            if column_str in row_map:
                count += row_map[column_str]

        return count

