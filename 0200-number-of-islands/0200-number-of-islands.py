class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        n = len(grid)
        m = len(grid[0])
        stack = []
        island = 0
        def isbound(r,c):
           if  0 <= r < n and 0 <= c < m:
                return True

        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    island += 1
                    grid[r][c] = '0'
                    stack.append((r,c))
                    while stack:
                        ro,co = stack.pop()
                        for x,y in direction:
                            new_r = ro + x
                            new_c = co + y
                            if isbound(new_r,new_c) and grid[new_r][new_c] =='1':
                                stack.append((new_r,new_c))
                                grid[new_r][new_c] = '0'
        return island

                                
