class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        t = 0
        col = set()
        down_diago = set()
        up_diago = set()

        final = []
        def backt(r):
            if r == n:
                temp = [['.']*n for _ in range(n)]
                for r,c in ans:
                    temp[r][c] = 'Q'
                temp = [''.join(temp[i]) for i in range(n)] 
            
                final.append(temp)
                return 
            for c in range(n):
                if c not in col and r+c not in up_diago and r-c not in down_diago:
                    ans.append([r,c])
                    col.add(c)
                    up_diago.add(r+c)
                    down_diago.add(r-c)
                    backt(r+1)
                    ans.pop()
                    col.remove(c)
                    up_diago.remove(r+c)
                    down_diago.remove(r-c)
       
        backt(0)
        return final



