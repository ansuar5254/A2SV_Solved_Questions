class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        direction = [(0,1),(0,-1),(1,0),(-1,0)] 
        island = 0           
        def dfs(row,col):
            if row < 0 or col < 0  or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == '0':
                return 

            grid[row][col] = '0'
            for x,y in direction:
                new_r = row + x
                new_c = col + y
                dfs(new_r,new_c)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':    
                    island += 1
                    dfs(r,c)
        return island

                