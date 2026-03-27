class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        up_dia = set()
        down_dia = set()
        ans = []
        temp = []
        def backTracking(r):
            if r == n:
                t = [['.']*n for _ in range(n)]
                for i,j in temp:
                    t[i][j] = 'Q'
                t = [''.join(ch) for ch in t]
                ans.append(t)

            for c in range(n):
                if c not in col and r+c not in up_dia and r-c not in down_dia:
                    temp.append([r,c])
                    up_dia.add(r+c)
                    col.add(c)
                    down_dia.add(r-c)
                    backTracking(r+1)
                    temp.pop()
                    up_dia.remove(r+c)
                    col.remove(c)
                    down_dia.remove(r-c)
        backTracking(0)
        return len(ans)

                





        