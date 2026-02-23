class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        ans = []
        total = rows * cols
        r = rStart
        c = cStart
        ans.append([r, c])
        steps = 1
        def first_row(r, c, step):   
            for _ in range(step):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            return r, c

        def last_col(r, c, step):   
            for _ in range(step):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            return r, c
        
        def last_row(r, c, step):    
            for _ in range(step):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            return r, c
        
        def first_col(r, c, step):   
            for _ in range(step):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    ans.append([r, c])
            return r, c
        
        while len(ans) < total:
            r, c = first_row(r, c, steps)
            r, c = last_col(r, c, steps)
            steps += 1
            
            r, c = last_row(r, c, steps)
            r, c = first_col(r, c, steps)
            steps += 1
        
        return ans
