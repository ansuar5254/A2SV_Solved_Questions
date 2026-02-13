class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] < 0:
                    count += 1
        return count 

        
