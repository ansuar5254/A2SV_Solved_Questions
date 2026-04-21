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

        def isb(r,c):
            for x,y in direction:
                new_r = r + x 
                new_c = c + y
                if 0 <= new_r < len(board) and 0 <= new_c < len(board[r]):
                    continue
                else:
                    return False
            return True

        not_sr = []

        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O' and not isb(r,c):
                    stack.append((r,c))
                    not_sr.append((r,c))
                    visited[r][c] = 1
                    while stack:
                        ro,co = stack.pop()
                        for x,y in direction:
                            new_r = ro + x
                            new_c = co + y
                            if isbound(new_r,new_c) and board[new_r][new_c] == 'O' and visited[new_r][new_c] == 0:
                                stack.append((new_r,new_c))
                                visited[new_r][new_c] = 1
                                not_sr.append((new_r,new_c))

        for r in range(len(board)):
            for c in range(len(board[r])):
                board[r][c] = 'X'

        for r,c in not_sr:
            board[r][c] = 'O'

        
                        

                            


                            




       

                    
                    
                   