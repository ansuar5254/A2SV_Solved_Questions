class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        def isboud(row,col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
                return True

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    for x,y  in direction:
                        new_r = r + x
                        new_c = c + y
                        if not isboud(new_r,new_c) or grid[new_r][new_c] == 0:
                            count += 1
        return count

                    


        



               

        
            
        
        
        