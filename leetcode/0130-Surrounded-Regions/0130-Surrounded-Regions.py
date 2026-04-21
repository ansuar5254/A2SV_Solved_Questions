class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        n = len(board)
        m = len(board[0])
        visited = [[0]*m for i in range(n)]
        stack = []
        def isbound(r,c):
            if 0 <= r < len(board) and 0 <= c < len(board[r]):
                return True
            return False

        not_sr = []
        def dfs():  
            while stack:
                ro,co = stack.pop()
                for x,y in direction:
                    new_r = ro + x
                    new_c = co + y
                    if isbound(new_r,new_c) and board[new_r][new_c] == 'O' and visited[new_r][new_c] == 0:
                        stack.append((new_r,new_c))
                        visited[new_r][new_c] = 1
                        not_sr.append((new_r,new_c))

        for c in range(m):
            if board[0][c] == 'O':
                stack.append((0,c))
                visited[0][c] = 1
                not_sr.append((0,c))
                dfs()

        for r in range(1, n):
            if board[r][m - 1] == 'O':
                stack.append((r,m-1))
                visited[r][m-1] = 1
                not_sr.append((r,m-1))
                dfs()
              

        for c in range(m - 2, -1, -1):
            if board[n - 1][c] == 'O':
                stack.append((n-1,c))
                visited[n-1][c] = 1
                not_sr.append((n-1,c))
                dfs()
                

        for r in range(n - 2, 0, -1):
            if board[r][0] == 'O':
                stack.append((r,0))
                visited[r][0] = 1
                not_sr.append((r,0))
                dfs()
                
                   
        for r in range(n):
            for c in range(m):
                board[r][c] = 'X'

        for r,c in not_sr:
            board[r][c] = 'O'