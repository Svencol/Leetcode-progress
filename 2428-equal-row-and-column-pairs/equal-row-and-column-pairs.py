class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n =len(grid)
        count = 0

        for row in grid:
            for col_index in range(n):
                column = []
                for row_index in range(n):
                    column.append(grid[row_index][col_index])
                if row == column:
                    count +=1
        return count
        