class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        pacific =[[0]*m for _ in range(n)]
        atlanctic = [[0]*m for _ in range(n)]

        def isbound(r,c):
           if  0 <= r < n and 0 <= c < m:
                return True

        def atlantic_dfs(r,c):
           
            atlanctic[r][c] = 1
            for x,y in direction:
                new_r = x + r
                new_c = y + c
                if isbound(new_r,new_c) and heights[r][c] <= heights[new_r][new_c] and atlanctic[new_r][new_c] == 0:
                    atlantic_dfs(new_r,new_c)

        def pacific_dfs(r,c):
            pacific[r][c] = 1
            for x,y in direction:
                new_r = x + r
                new_c = y + c
                if isbound(new_r,new_c) and heights[r][c] <= heights[new_r][new_c] and pacific[new_r][new_c] == 0:
                    pacific_dfs(new_r,new_c)

        for i in range(m):
            pacific_dfs(0,i)

        for i in range(n):
            pacific_dfs(i,0)

        for i in range(m):
            atlantic_dfs(n-1,i)

        for i in range(n):
            atlantic_dfs(i,m-1)


        ans = []
        for r in range(n):
            for c in range(m):
                if atlanctic[r][c]  and pacific[r][c]:
                    ans.append([r,c])
        return ans