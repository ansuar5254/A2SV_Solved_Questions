class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
       


        minu = 0
        n = len(grid)
        m = len(grid[0])
        q = deque()
        direction = ((0,1),(0,-1),(1,0),(-1,0))
        def isbound(r,c):
            if 0 <= r < n and 0 <= c < m:
                return True
        fresh = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append((r,c))

        if fresh == 0:
            return 0

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for x,y in direction:
                    nr  = x + r
                    nc = y + c
                    if isbound(nr,nc) and  grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2

            minu += 1

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    return -1

        return minu-1
 
    