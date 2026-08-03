from collections import Counter

class Solution:
    def equalPairs(self, grid):

        row_count = Counter(tuple(row) for row in grid)

        count = 0

        n = len(grid)

        for j in range(n):

            column = []

            for i in range(n):
                column.append(grid[i][j])

            count += row_count.get(tuple(column), 0)
        return count